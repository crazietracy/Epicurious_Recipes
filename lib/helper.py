diets = ['alcoholic','dairy free','dairy','fat free', 'healthy','high fiber','kid-friendly','kidney friendly','kosher','low cal','low carb','low cholesterol','low fat','low sodium','low sugar','low/no sugar','no sugar added','non-alcoholic','organic','paleo','peanut free','pescatarian','soy free','soy','sugar conscious','tree nut free','tree nut','vegan','vegetarian','wheat/gluten-free']


ingredients = ['almond','amaretto','anchovy','anise','apple juice','apple','apricot','artichoke','arugula','asian pear','asparagus','avocado','bacon','banana','barley','basil','bass','beef rib',
'beef shank','beef tenderloin','beef','beet','bell pepper','blackberry','blue cheese','blueberry','bok choy','bourbon','brandy','bread','breadcrumbs','brie','brisket','broccoli rabe','broccoli','brown rice',
'brussel sprout','buffalo','bulgur','burrito','butter','buttermilk','butternut squash','butterscotch/caramel','cabbage','calvados','campari','cantaloupe','capers','caraway','cardamom','carrot','cashew','cauliflower','caviar','celery','chambord','champagne','chard','chartreuse','cheddar','cherry','chestnut','chicken','chickpea','chile pepper','chili','chive','chocolate','cilantro','cinnamon','citrus','clam','clove','coconut','cod','coffee','cognac/armagnac','collard greens','coriander','corn','cornmeal','cottage cheese','couscous','crab','cranberry sauce','cranberry','cream cheese','créme de cacao','crêpe','cr��me de cacao','cucumber','cumin','currant','curry',
'date',
'dill',
'dried fruit',
'duck',
'eau de vie',
'egg nog',
'egg',
'eggplant',
'endive',
'escarole', 
'fennel',
'feta',
'fig',
'fontina',
'frangelico',
'garlic',
'gin',
'ginger',
'goat cheese',
'goose',
'gouda',
'grand marnier',
'granola',
'grape',
'grapefruit',
'grappa',
'green bean',
'green onion/scallion',
'ground beef',
'ground lamb',
'guava',
'halibut',
'ham',
'hamburger',
'hazelnut',
'hominy/cornmeal/masa',
'honey',
'honeydew',
'horseradish',
'hot pepper',
'hummus',
'iced coffee',
'iced tea',
'jalapeño',
'jerusalem artichoke',
'jícama',
'kahlúa',
'kale',
'kirsch',
'kiwi',
'kumquat',
'lamb chop',
'lamb shank',
'lamb',
'leek',
'lemon juice',
'lemon',
'lemongrass',
'lentil',
'lettuce',
'lima bean',
'lime juice',
'lime',
'lingonberry',
'lobster',
'lychee',
'macadamia nut',
'mango',
'maple syrup',
'marsala',
'marscarpone',
'marshmallow',
'mayonnaise',
'mezcal',
'midori',
'mint',
'molasses',
'monterey jack',
'mozzarella',
'mushroom',
'mussel',
'mustard greens',
'nectarine',
'nutmeg',
'oat',
'oatmeal',
'octopus',
'okra',
'olive',
'onion',
'orange juice',
'orange',
'oregano',
'orzo',
'oyster',
'papaya',
'paprika',
'parmesan',
'parsley',
'parsnip',
'passion fruit',
'pea',
'peach',
'peanut butter',
'peanut',
'pear',
'pecan',
'pepper',
'pernod',
'persimmon',
'pickles',
'pine nut',
'pineapple',
'pistachio',
'plantain',
'plum',
'poblano',
'pomegranate juice',
'pomegranate',
'poppy',
'pork chop',
'pork rib',
'pork tenderloin',
'pork',
'port',
'potato',
'prosciutto',
'prune',
'pumpkin',
'quail',
'quince',
'quinoa',
'rabbit',
'rack of lamb',
'radicchio',
'radish',
'raisin',
'raspberry',
'red wine',
'rhubarb',
'rice',
'ricotta',
'rosemary',
'rosé',
'rum',
'rutabaga',
'rye',
'saffron',
'sage',
'sake',
'salmon',
'sardine',
'scallop',
'scotch',
'semolina',
'sesame oil',
'sesame',
'shallot',
'sherry',
'shrimp',
'snapper',
'sorbet',
'sour cream',
'sourdough',
'soy sauce',
'spinach',
'squash',
'squid',
'strawberry',
'sugar snap pea',
'sweet potato/yam',
'swiss cheese',
'swordfish',
'tamarind',
'tangerine',
'tapioca',
'tarragon',
'tea',
'tequila',
'thyme',
'tilapia',
'tofu',
'tomatillo',
'tomato',
'triple sec',
'trout',
'tuna',
'turkey',
'turnip',
'vanilla','veal','venison','vermouth','vodka','walnut','wasabi','watercress','watermelon','whiskey','white wine','wild rice','yellow squash','yogurt','yuca','zucchini','bean','berry','bitters','bran','cheese','fish','fortified wine','fruit juice','fruit',
'game','grains','herb','jam or jelly','leafy green','legume','liqueur','milk/cream','meat','melon','muffin','mustard','noodle','nut','phyllo/puff pastry dough','potato salad','poultry sausage','poultry','root vegetable','sausage','seafood','seed','shellfish','spice','steak','tropical fruit','vegetable','vinegar','whole wheat','wine']

def new_label_array(x, some_list):
    try:
        label_list = [i for i in x if i in some_list]
    except:
        label_list = [i for i in x if i in some_list]
    return list(label_list)
