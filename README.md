# Bilaf

Back-End application developed by utilizing the following: 
- Python
- Django Framework
- PostgreSql

A website dedicated to promoting and selling family brands products. Bilaf serves as a bridge between consumers and families; rather than utilizing other platforms to reach them, Bilaf gives a more convenient approach to reach them. 



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
- Chat between the client and vendor after the purchase is completed.
- Rate the order.
- Viewing past orders.
## Product Owner
- Editing their products.
- Orders will be approved based on the given Delivery\Pickup availability. 
- Chat with client.
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
- As a Client, Or bilter the brands based on a specific cuisine.
- As a Client, Or edit the cart before making a purchase.
- As a Client, Or making a purchase.
- As a Client, Or view my order status.
- As a Client, Or chatting with the vendor.
- As a Client, Or rate the order.
- As a Client, Or viewing past orders.
## Product Owner
- As an owner, I can edit my products.
- As an owner, Or provide an indication on my Delivery\Pickup availability, for order approvals.
- As an owner, Or view my brand's performance dashboard.
- As an owner, Or reply to the client's review.
- As an owner, Or chat with the client.
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

### merchant_profile:
- id
- user =  OneToOneField(User)
- merchant_name = char_field
- logo = image
- about = text_field
- city = char_field
- address = OneToOneField(Address)

### customer_profile:
- id
- user =  OneToOneField(User)
- city = char_field
- address = OneToOneField(address)
- gender = char_field
- birthday = date
- created_at = date
- last_order_date = date

### Address:
- id
- merchant = foreignKey (merchant_profile)
- customer = foreignKey (customer_profile)
- longitude = float
- latutude = float 
- district = char_field
- description = text_field

### product:
- id
- name = char_field
- category = foreignKey (category)
- logo = images
- price = integer_field
- description = text_field
- quantity = integer_field

### category:
- id
- name

### cart: 
- id
- merchant = foreignKey (mechant_profile)
- customer = foreignKey (customer_profile)
- status =  integrer_filed
- item = ManyToMany (cart_items)
- created_at = date
- due_date = date
- total = integer_filed
- delivery_option = char_field
- payment_option = char_field

### cart_item:
- id
- cart = foreignKey (cart)
- product = foreignKey (product)

### order:
- id
- cart = foreignKey (merchant_profile)
- status = char_field
- done_at =date
- decline_reason = char_field 

### review:
- id
- merchant = foreignKey (mechant_profile)
- order = foreignKey (order)
- product = foreignKey (product)
- rating = integer_field
- comment = text_field

 

# Members

- Omar Ali : https://github.com/Omar-Ali99
- Faisal Al-Hussain: https://github.com/faisal-alhussain
- Abdullah Al-Saab: https://github.com/amalsaab
- Mohammed Al-Khabbaz: https://github.com/97MK


## UML diagrams

 Use-Case Diagram:
 
 
 ![Screenshot 2023-06-13 220053](https://github.com/Omar-Ali99/Bilaf/assets/101348008/afd44a30-070a-432d-9a4b-b6e08ac4f712)
 
 
 ER Diagram:



![Screenshot 2023-06-13 230904](https://github.com/Omar-Ali99/Bilaf/assets/101348008/289d7905-93f6-412b-b74f-0d55ed6d43fe)




