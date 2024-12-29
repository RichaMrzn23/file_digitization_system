from rest_framework. permissions import BasePermission
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import permissions

# class IsAuthenticatedOrReadOnly(BasePermission):
     
#      def has_permission(self, request, view):
#          return request.user and request.user.is_authenticated

class IsAdminOnly(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role == "admin")
    
class IsManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
      if request.method in  permissions.SAFE_METHODS:
            return True
      return (request.user.is_authenticated and request.user.role == 'manager')
    
class IsManagerOnly(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role == "manager")
    
# class IsRegularUserOrReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return request.user.is_authenticated and request.user.role == "regula_user"
    
# class IsRegularUserOnly(BasePermission):
#     def has_permission(self, request, view):
#             return request.user.is_authenticated and request.user.role == "regular_user"
    
    
class IsRegularUserOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
           return False
        
        role = getattr(request.user, 'role', None)
        if role != "regular_user":
            return False
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.method == "POST" and getattr(view, "allow_comments", False):
            return True
        
        return False