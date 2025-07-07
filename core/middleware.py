from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define allowed URLs for each role
        allowed_urls = {
            'SUPERADMIN': [
                reverse('superadmin_dashboard'),
                # Add other URLs for SUPERADMIN
            ],
            'ADMIN': [
                reverse('admin'),
                # Add other URLs for ADMIN
            ],
            # 'ADMIN': [
            #     reverse('department_admin_dashboard'),
            #     # Add other URLs for ADMIN
            # ],
            'SUBADMIN': [
                reverse('sub_admin_dashboard'),
                # Add other URLs for SUBADMIN
            ],
        }

        # Exempt URLs (e.g., mobile_verification, logout)
        exempt_urls = [
            reverse('mobile_verification'),
            reverse('logout'),
        ]

        # Debugging: Print session data and current URL
        print(f"Session Data: {request.session}")
        print(f"Current URL: {request.path_info}")

        # # Bypass middleware for exempt URLs
        if request.path_info in exempt_urls:
            return self.get_response(request)

        # # Check if the user is authenticated (mobile is in session)
        if not request.session.get('mobile'):
            messages.error(request, 'You need to verify your mobile number.')
            return redirect('mobile_verification')  # Redirect to mobile verification if not authenticated

        # # Check if the user has a valid role
        # user_role = request.session.get('role')
        # if user_role not in allowed_urls:
        #     messages.error(request, 'You do not have permission to access this page.')
        #     return redirect('mobile_verification')  # Redirect to mobile verification if no valid role

        # # Check if the current URL is allowed for the user's role
        # if request.path_info not in allowed_urls[user_role]:
        #     messages.error(request, 'You do not have permission to access this page.')
        #     return redirect('mobile_verification')  # Redirect to mobile verification if URL is not allowed

        # Allow access to the requested URL
        response = self.get_response(request)
        return response