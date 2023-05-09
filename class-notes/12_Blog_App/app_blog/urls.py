from rest_framework import routers
from .views import(
    BlogCategoryView,
    BlogPostView,
    BlogCommentView,
)
router=routers.DefaultRouter()
router.register('categories',BlogCategoryView)
router.register('posts',BlogPostView)
router.register('comments',BlogCommentView)


# urlpatterns = [
#     # path('blog/', ),
# ]
# router dışında bir şey yoksa
urlpatterns = router.urls