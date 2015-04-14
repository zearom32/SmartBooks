from django.conf.urls import url,patterns

from books import views

urlpatterns = patterns('',
        url(r'^$',views.index,name='index'),
        url(r'^register$',views.register,name="register"),
        url(r'^login$',views.Login,name="login"),
        url(r'^homepage$',views.homepage,name="homepage"),
        url(r'^bookinfo$',views.bookinfo,name="bookinfo"),
        url(r'^search_book$',views.search_book,name="search_book"),
        url(r'^books_of_a_seller$',views.books_of_a_seller,name="books_of_a_seller"),
        url(r'^sellers_of_a_book$',views.sellers_of_a_book,name="sellers_of_a_book"),
        url(r'^goodsinfo$',views.goodsinfo,name="goodsinfo"),
        url(r'^buy$',views.buy,name="buy"),
        url(r'^sell$',views.sell,name="sell"),
        url(r'^sellerinfo$',views.sellerinfo,name='sellerinfo'),

##develop
        #url(r'^deleteallusers$',views.deleteallusers, name = 'deleteallusers'),
        url(r'^addbooks$',views.addbooks,name='addbooks'),
        url(r'^updatebooks$',views.updatebooks,name="updatebooks"),
        )
