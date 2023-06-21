# Bilaf

Back-End application developed by utilizing the following: 
- Python
- Django Framework
- PostgreSql

A website dedicated to promoting and selling family-brand products. Bilaf serves as a bridge between consumers and families; rather than utilizing other platforms to reach them, Bilaf provides a more convenient approach to reaching them. 



# Feature List
## Unregistered Client
- Browsing the brands.
- Browsing the brand's products.
- Searching for a product or brand.
- Filtering the brands based on a specific cuisine.
## Client 
- Browsing the brands.
- Browsing the brand's products.
- Searching for a product or brand.
- Filtering the brands based on a specific cuisine.
- Editing the cart before making a purchase.
- Making a purchase.
- Viewing the order status.
- Rate the order.
- Viewing past orders.
## Product Owner
- Editing their products.
- Orders will be approved based on the given Delivery\Pickup availability. 
- Reply to client's review
- Performance dashboard for the brand.
## Admin
- Accept\Decline the merchant.
- Decline certain orders.
- Performance dashboard for all the brands.
- Replying to the client's review.

# User Stories
## Unregistered Client
- As a visitor, I can browse the brands.
- As a visitor, Or browse the brand's products.
- As a visitor, Or search for a product or brand.
- As a visitor, Or filter the brands based on a specific cuisine.
- As a visitor, Or register to make any purchases.
## Client
- As a Client, I can browse the brands.
- As a Client, Or browse the brand's products.
- As a Client, Or search for a product or brand.
- As a Client, Or filter the brands based on a specific cuisine.
- As a Client, Or edit the cart before making a purchase.
- As a Client, Or making a purchase.
- As a Client, Or view my order status.
- As a Client, Or rate the order.
- As a Client, Or viewing past orders.
## Product Owner
- As an owner, I can edit my products.
- As an owner, Or provide an indication on my Delivery\Pickup availability, for order approvals.
- As an owner, Or view my brand's performance dashboard.
- As an owner, Or reply to the client's review.
## Admin
-  As the Admin, I can accept\decline the merchant that wants to regsiter on my platform.
-  As the Admin, Or decline certain orders.
-  As the Admin, Or view the performance dashboard for all the brands.
# Website Wireframe
[Figma's link for the wireframe](https://www.figma.com/file/Pyn0ZtL60KFQpZrYi6JKpK/Bilaf?type=design&node-id=0-1&t=6D7QYlY7L2egdGfx-0)

# Models 
### user:
- id
- first_name
- last_name
- email
- password

### Profile:
- user = OneToOneField(User)
- phone_number = CharField
    
### Store:
- owner = ForeignKey(User)
- store_name = CharField
- category = (CHOICES)
- logo = ImageField
- about = TextField
- pick_up_enabled = BooleanField(default=True)
- delivery_enabled = BooleanField(default=True)
- twitter_link = URLField
- instagram_link = URLField
- snapchat_link = URLField

### Categories:
- name = CharField
- logo = ImageField
- store = ForeignKey(Store)

### Product:
- store = ForeignKey(Store)
- category = ForeignKey(Categories)
- price = FloatField
- quantity = IntegerField
- is_active = BooleanField(default=True)
- name = CharField
- description = TextField
- image = ImageField

### Cart:
- DELIVERY_CHOICES = (CHOICES)
- PAYMENT_CHOICES = (CHOICES)
- store = ForeignKey(Store)
- customer = ForeignKey(User)
- status = (CHOICES)
- created_at = models.DateTimeField(auto_now_add=True)
- due_date = models.DateTimeField(blank=True, null=True)

### CartItem:
- cart = ForeignKey(Cart)
- product = ForeignKey(Product)
- quantity = PositiveIntegerField
- price = PositiveIntegerField


# Members

- Omar Ali : https://github.com/Omar-Ali99
- Faisal Al-Hussain: https://github.com/faisal-alhussain
- Abdullah Al-Saab: https://github.com/amalsaab
- Mohammed Al-Khabbaz: https://github.com/97MK


## UML diagrams

 Use-Case Diagram:
 
 
 ![Screenshot 2023-06-13 220053](https://github.com/Omar-Ali99/Bilaf/assets/101348008/afd44a30-070a-432d-9a4b-b6e08ac4f712)
 
 
 ER Diagram:


![Screenshot 2023-06-21 222425](https://github.com/Omar-Ali99/Bilaf/assets/101348008/791d79a3-873b-4679-af28-d2736cead514)





