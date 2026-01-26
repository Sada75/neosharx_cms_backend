from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
import requests
from django.conf import settings



User = get_user_model()


@csrf_exempt
@api_view(["POST"])
def signup(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    if User.objects.filter(email=email).exists():
        return Response({"error": "Email already exists"}, status=400)

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
    )

    refresh = RefreshToken.for_user(user)

    return Response({
        "token": str(refresh.access_token),
        "refresh": str(refresh),
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }
    }, status=201)




@csrf_exempt
@api_view(["POST"])
def google_callback(request):
    print("REQUEST DATA:", request.data)
    code = request.data.get("code")

    if not code:
        return Response({"error": "Authorization code missing"}, status=400)

    # 1️⃣ Exchange code → access token
    token_res = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        },
    )

    print("GOOGLE TOKEN STATUS:", token_res.status_code)
    print("GOOGLE TOKEN BODY:", token_res.text)

    token_data = token_res.json()
    access_token = token_data.get("access_token")

    if not access_token:
        return Response({"error": "Failed to obtain access token"}, status=400)

    # 2️⃣ Fetch user info
    userinfo_res = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    userinfo = userinfo_res.json()

    email = userinfo.get("email")
    name = userinfo.get("name", "")
    picture = userinfo.get("picture")

    if not email:
        return Response({"error": "Email not available"}, status=400)

    # 3️⃣ Create or fetch user
    user, created = User.objects.get_or_create(
        email=email,
        defaults={
            "username": name,
        },
    )

    if created:
        user.set_unusable_password()
        user.save()

    # 4️⃣ Issue JWT
    refresh = RefreshToken.for_user(user)

    return Response({
        "token": str(refresh.access_token),
        "refresh": str(refresh),
        "user": {
            "id": user.id,
            "email": user.email,
            "username": user.username,
        }
    })
