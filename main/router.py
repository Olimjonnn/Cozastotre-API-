from rest_framework import routers
from main.views import *

router = routers.DefaultRouter()

router.register("slider", SliderView)
router.register("product", ProductView)
router.register("categories", CategoriesView)
router.register("info", InfoView)
router.register("newsletters", NewslettersView)
router.register("blog", BlogView)
router.register("about", AboutView)
router.register("contact", ContactView)
router.register("cart", CartView)
router.register("wishlist", WishlistView)