from rest_framework import routers
from .views import BrandView, CategoryView, FirmView, ProductView, TransactionView


router = routers.DefaultRouter()
router.register('transaction', TransactionView)
router.register('category', CategoryView)
router.register('brand', BrandView)
router.register('firm', FirmView)
router.register('product', ProductView)

urlpatterns = [

]

urlpatterns += router.urls
