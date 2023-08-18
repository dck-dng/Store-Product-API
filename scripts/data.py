import random
import json

def generate_rgb_hex_list(a, b):
    rgb_hex_list = []
    
    for i in range(a, b):
        rgb_hex = format(i, '06x')
        rgb_hex_list.append(rgb_hex)
                
    return rgb_hex_list

hex_value_colors = generate_rgb_hex_list(1, 1000)
product_images = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMIAG8BdpFXEbGJhS2JiBMrqysJ5Rby8mhdg&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5GuGTdeY8MTGuJ6r2zywehrbVIFlJgMBUsEhiL93phYeeGQidzHPSScixwVprt-KQKZQ&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYR8a7PDmL6mGtD6HSZNmQbMwF0mXanru9rZjuNq4O4QiNRkwUgBV7Dfrx7nk46wGzaHY&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlylhHb85zbbiNRGpGTbQbMSTAHo80RVWkOQ&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYJ2oM4DJYwTlqzrATnF7HAJ1kAxysg27MjQ&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbsCEOUSzTnjyiiStU-kRmVRJLCQEi1rQdaQ&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS73UmP_-lBjG7oBLDBuv6fQDlKtiOa2CrxPA&usqp=CAU",
    "https://pgdphurieng.edu.vn/wp-content/uploads/2023/05/minions-rise-of-gru-7.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuw8aXHeJjdE_7bIqXJU16js5ETNJMZki2Nvs_rH13k2sWQmKIjhpdI5bGKwmu7K1x1Cs&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7pfiaAJBtY20UGL_195ubi3QprOL1-qSOEA&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiKD-e8gVTgD4iQkbd_dLwoloZZrezKt1IkQ&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8_K6GNojjsAh-MYkHbU4rYuX6VOV_e4a6-g&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTow4Zh-5-lY2zLb0i4tFwRGI33WsVKUKl50g&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStD0CzPQkf6rpbSFX1EbDVqXIXnASx1tGIXQ&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ041Gpm8K4dVhKcGHUIjwMTlV3ISCZgMVvRg&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfoj_XCIoJJa4VKRC0nqTNvoo1aXRU9p9Mdv1sedfaseq_rYKl6iinF_LEh_6Aewh9rD8&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQINZxVC7BbbroX2tAHXHykjTyzAyLWS7AfEVX4bmRKMAeWck0d64n5yoUvH4Qj9glM0uA&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6KBV2ANxkvQxK3LtQDF2SveLUvk5a2OdA_g&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQ5ctqhLPNS1IZPUwOxNWMwy52iQyHGYUgKw&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTe5yES6ZB-9W8avq31Jp1g2vd1z7eo7GeNqA&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeoecV6BTnIKRawD5b-yL8Cp5fQAltKGeNSg&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4oLH1So5ZYocGeHOgBMNyURwkmiOkX1dlOA&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSELTg-NKPCjZym0dwx1Z4WntNDSofMO7dRLQ&usqp=CAU"
]
# copy ở trong này
add_images, delete_images, add_colors, delete_colors = [], [], [], []
for i in range(random.randint(1, 6)):  
    add_images.append(random.choice(product_images))

for i in range(random.randint(1, 6)):  
    delete_images.append(random.choice(product_images))

for i in range(random.randint(5, 6)):   
    add_colors.append(random.choice(hex_value_colors))

for i in range(random.randint(1, 5)):   
    delete_colors.append(random.choice(hex_value_colors))




product_name=["Sofa", "Dining Table", "Bed", "Bookshelf", "Coffee Table", "Armchair", 
               "Wardrobe", "TV Stand", "Nightstand", "Desk", "Sectional Sofa", 
               "Cabinet", "Ottoman", "Console Table", "End Table", "Rocking Chair", 
               "Dresser", "Bunk Bed", "Chaise Lounge", "Folding Chair", "Bar Stool", 
               "Sideboard", "Futon", "Accent Chair", "Credenza", "Hall Tree", "Lounge Chair", 
               "Platform Bed", "Recliner", "Vanity Table", "Hammock", "Bean Bag", "Shoe Rack", 
               "Pouf", "Bookcase", "Buffet Table", "Chesterfield Sofa", "Folding Table", 
               "Murphy Bed", "Chandelier", "Nesting Tables", "Storage Bench", "Step Stool", 
               "Gaming Chair", "Daybed", "Bar Cart", "Love Seat", "Room Divider"]

product_price = []

for i in range(100):
    price = round(random.uniform(10000, 1000000), 2)  # Generating random price between 100 and 1000
    product_price.append(price)

product_company = ["StellarTech", "QuantumSolutions", "SwiftFusion", "InnovateWave", "NexusIndustries", "FusionSynergy", 
                   "ApexDynamics", "QuantumCore", "PrimeInnovations", "NovaVentures", "ProdigySystems", "AlphaSolutions",
                    "InfinityEnterprises", "SpectrumTech", "VanguardGroup", "VisionaryIndustries", "AlphaWave", "DynamoInnovations", 
                    "QuantumHorizon", "VertexGlobal", "NebulaDynamics", "EchelonSolutions", "OmegaInnovate", "QuantumStride", 
                    "SynergyWorks", "ZenithEnterprises", "FusionX", "OptimaTech", "PinnacleInnovations", "OrionIndustries",
                    "HyperionSolutions", "InnovateAxis", "QuantumNexa", "AlphaPrime", "SpectrumVentures", "EonSynergy", 
                    "InnovareTech", "StellarPath", "ProximaIndustries", "VelocityWave", "FusionInnovations", "QuantumQuest", 
                    "AstralEnterprises", "VisionWave", "InnovateFusion", "SynergeticSystems", "AlphaDynamics", "QuantumStrive", "NebulaNex", "ApexInnovations"]

product_description = [
    "Elevate your living space with this exquisite and modern home decor piece that seamlessly combines form and function. Crafted with attention to detail, its intricate design and premium materials add a touch of sophistication to any room, creating an ambiance of elegance and style.",
    "Experience the epitome of technological advancement with this cutting-edge electronics device. Designed to push the boundaries of innovation, it delivers unparalleled performance, seamless connectivity, and a user-friendly interface that puts the power of the future in your hands.",
    "Step into the world of high fashion with this meticulously designed clothing item that captures the latest trends and reflects your individual style. Its timeless elegance and superior craftsmanship ensure both comfort and confidence, making it the perfect addition to your wardrobe.",
    "Indulge in a luxurious self-care routine with this premium health and beauty product that pampers your senses and revitalizes your skin. Infused with natural ingredients and advanced formulations, it promises a rejuvenating experience that leaves you feeling refreshed and radiant.",
    "Ignite your passion for adventure with this high-performance sports and outdoors equipment that's built to withstand the elements and conquer new horizons. Whether you're a seasoned athlete or a weekend explorer, this gear empowers you to push your limits and embrace the thrill of the outdoors.",
    "Transform your vehicle into a masterpiece of engineering with this top-of-the-line automotive accessory. Engineered for both style and functionality, it enhances your driving experience while making a bold statement on the road.",
    "Immerse yourself in a captivating world of storytelling with this thought-provoking book that delves deep into the human experience. Its eloquent prose and intricate plot twists keep you engaged from cover to cover, leaving you inspired and introspective.",
    "Nurture creativity and imagination with this meticulously crafted toy or game that sparks joy across generations. Designed to be both entertaining and educational, it encourages interactive play and exploration, fostering a sense of wonder and learning.",
    "Savor the ultimate culinary experience with this collection of gourmet food and beverage selections that tantalize your taste buds and transport you to a world of flavor. From delectable treats to exotic blends, each item is a celebration of taste and craftsmanship.",
    "Adorn yourself with timeless elegance by wearing this exquisite piece of jewelry that encapsulates the essence of luxury. Meticulously designed and crafted, it embodies sophistication and grace, making it the perfect accent for any occasion.",
    "Elevate your living space with this meticulously crafted furniture item that marries functionality with aesthetics. Its ergonomic design and premium materials ensure comfort and durability, while its versatile style effortlessly complements your interior decor.",
    "Effortlessly simplify your daily routine with this innovative and reliable appliance that streamlines tasks and enhances efficiency. Engineered for convenience, it takes care of household chores, giving you more time to focus on what matters most.",
    "Stay organized and productive with this comprehensive collection of office supply essentials that cater to your professional needs. From sleek writing instruments to ergonomic accessories, these items are designed to optimize your workspace and enhance productivity.",
    "Show your furry friend some love with these premium pet supplies that prioritize comfort, safety, and happiness. From cozy beds to interactive toys, each item is thoughtfully chosen to enhance your pet's well-being and bring joy to their everyday life.",
    "Embark on a journey of gardening success with this essential set of tools that empowers you to create a flourishing oasis in your own backyard. From planting to nurturing, these tools ensure a rewarding and satisfying gardening experience.",
    "Embark on new adventures with confidence using this versatile and durable travel and luggage item. Designed for convenience and functionality, it offers ample storage space and innovative features that simplify your travel experience, making every journey memorable.",
    "Unleash your creativity and skills with this comprehensive collection of crafting and hobby materials that cater to enthusiasts of all levels. From DIY projects to intricate creations, these materials provide the foundation for endless artistic exploration.",
    "Cater to your baby's needs with this comprehensive collection of safe and comfortable baby products that prioritize their well-being and comfort. From soothing essentials to practical accessories, each item is designed to make parenting a joyful and rewarding experience.",
    "Achieve your fitness goals with this state-of-the-art fitness equipment that brings the gym experience to the comfort of your home. Designed for maximum effectiveness and versatility, it empowers you to embrace an active lifestyle and pursue your health aspirations.",
]

product_category = ["Home Decor", "Electronics", "Fashion", "Health & Beauty", "Sports & Outdoors", "Automotive", 
                     "Books", "Toys & Games", "Food & Beverages", "Jewelry", "Furniture", "Appliances", "Office Supplies", 
                     "Pet Supplies", "Gardening", "Travel & Luggage", "Crafts & Hobbies", "Baby Products", "Fitness", 
                     "Music", "Movies", "Art & Collectibles", "Electrical", "Outdoor Gear", "Kitchenware", "Party Supplies", 
                     "Tools & Hardware", "Stationery", "Personal Care", "Footwear", "Watches", "Home Improvement", "Cookware", 
                     "Gadgets", "Stationery", "Gifts", "Accessories", "Lifestyle", "Electrical", "Bed & Bath", "Stationery", 
                     "Entertainment", "Home Organization", "Home Cleaning", "Home Textiles", "Cosmetics", "Fashion Accessories", "Pet Care", "DIY Kits"]

product_update_partial = {
    "add_images": add_images,
    "delete_images": delete_images,
    "add_colors": add_colors,
    "delete_colors": delete_colors
}

# print(json.dumps(product_update_partial))

product_update_or_add = {
    "name": random.choice(product_name),
    "price": random.choice(product_price),
    "company": random.choice(product_company),
    "description": random.choice(product_description),
    "category": random.choice(product_category),
}

print(json.dumps(product_update_or_add))