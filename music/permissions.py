from rest_framework import permissions

class IsArtistOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.artist == request.user



class IsNotAdmin(permissions.BasePermission):

	def has_permission(self, request, view, obj):
		def has_permission(self, request, view):
			return bool(request.artist) == request.user