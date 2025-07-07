from django.shortcuts import redirect
from django.contrib import messages

def role_required(allowed_roles):
    """
    Decorator to restrict access to views based on user roles.
    :param allowed_roles: List of roles allowed to access the view (e.g., ['SUPERADMIN', 'ADMIN'])
    """
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            # Check if the user is authenticated (mobile is in session)
            if not request.session.get('mobile'):
                messages.error(request, 'You need to verify your mobile number.')
                return redirect('mobile_verification')

            # Check if the user has one of the allowed roles
            user_role = request.session.get('role')
            if user_role not in allowed_roles:
                messages.error(request, 'You do not have permission to access this page.')
                return redirect('mobile_verification')

            # If the user is authorized, call the view function
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator