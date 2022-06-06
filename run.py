from booking.booking import Booking
with Booking() as bot:
    bot.landing_page()
    bot.select_category('Phones & Tablets') 
    bot.search_brand('Samsung')
    bot.select_items()