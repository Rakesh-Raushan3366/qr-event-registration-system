from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def role_required(allowed_roles):
    """
    Decorator to restrict access to views based on user roles.
    :param allowed_roles: List of roles allowed to access the view (e.g., ['SUPERADMIN', 'ADMIN'])
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            mobile = request.session.get('mobile')

            # Check if mobile is missing or invalid
            if not mobile or not mobile.isdigit() or len(mobile) != 10:
                messages.error(request, 'Invalid or expired session. Please verify your mobile number again.')

                # Try to detect app origin from session and redirect accordingly
                source_app = request.session.get('source_app')
                if source_app == 'register_samautkarsh':
                    return redirect('register_samautkarsh:mobile_verification')
                elif source_app == 'updated_registration':
                    return redirect('updated_registration:mobileverification')
                else:
                    return redirect('updated_registration:home')  # fallback if no app info available

            # Check if the user has an allowed role
            user_role = request.session.get('role')
            if user_role not in allowed_roles:
                messages.error(request, 'You do not have permission to access this page.')
                return redirect('mobile_verification')

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
