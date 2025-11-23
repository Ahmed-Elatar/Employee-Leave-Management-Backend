from .base import *








####################################################################################################
##################                  Authentication


# {
#   "username": "ahmed",
#   "password1": "StrongPassword123!",
#   "password2": "StrongPassword123!",
#   "name": "Ahmed Elatar",
#   "email": "ahmed@example.com",
#   "company": 1,
#   "role": "hr",
#   "joining_date": "2025-11-23"
# }
# sign-up 
class SignupAPIView(APIView):
    def post(self, request):
        form = SignupForm(request.data)
        if form.is_valid():
            user = form.save()
            # Optionally log the user in immediately
            login(request, user)
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"errors": form.errors}, status=status.HTTP_400_BAD_REQUEST)










# {
#   "username": "ahmed",
#   "password": "StrongPassword123!"
# }


# login 

class LoginAPIView(APIView):
    def post(self, request):
        form = LoginForm(request.data)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user:
                login(request, user)
                return Response({"message": "Login successful", "username": user.username})
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({"errors": form.errors}, status=status.HTTP_400_BAD_REQUEST)



# logout page
def user_logout(request):
    logout(request)
    return redirect('index')