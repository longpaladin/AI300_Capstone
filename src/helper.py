def datatype_conversion(form_input):
    num_dependents = int(form_input['num_dependents'])
    num_referrals = int(form_input['num_referrals'])
    tenure_months = int(form_input['tenure_months'])
    total_monthly_fee = float(form_input['total_monthly_fee'])
    age = int(form_input['age'])
    contract_type = form_input['contract_type']
    city = form_input['city']
    print(f"After datatype conversion: {[num_dependents, num_referrals, tenure_months, total_monthly_fee,age, contract_type, city]}")
    return [num_dependents, num_referrals, tenure_months, total_monthly_fee,age, contract_type, city]

def sorted_cities():
    cities = ['Camarillo', 'Napa', 'Sheridan', 'La Mesa', 'Los Olivos', 'Woodlake', \
        'Ahwahnee', 'Alpaugh', 'Parlier', 'Moss Beach', 'Los Angeles', 'Calexico', \
        'Fremont', 'Visalia', 'Lodi', 'Calistoga', 'Farmington', 'Tulelake', \
        'Ojai', 'Desert Hot Springs', 'Santa Rosa', 'Wilmington', 'West Point', \
        'Morongo Valley', 'Palo Verde', 'Valyermo', 'Cambria', 'San Diego', \
        'Monterey Park', 'Big Oak Flat', 'North Highlands', 'Glenhaven', 'Alhambra', \
        'Santa Monica', 'Stockton', 'Fallbrook', 'Randsburg', 'La Mirada', 'Tuolumne', \
        'Del Rey', 'Oceano', 'Clarksburg', 'Garden Grove', 'Indio', 'Oxnard', 'Los Gatos', \
        'Clovis', 'Woodland Hills', 'Midway City', 'Oakland', 'San Anselmo', 'Lake Elsinore', \
        'Downey', 'Challenge', 'Santa Clara', 'Perris', 'Clio', 'Lompoc', 'Pilot Hill', \
        'Mission Hills', 'Pescadero', 'Aromas', 'Badger', 'La Puente', 'Berry Creek', \
        'Fulton', 'Gardena', 'Santa Ana', 'Darwin', 'San Bernardino', 'Upland', 'El Dorado Hills', \
        'Palmdale', 'Hoopa', 'Burnt Ranch', 'Santa Margarita', 'Ione', 'San Mateo', 'Santa Cruz', \
        'Sherman Oaks', 'Thornton', 'Colusa', 'Lancaster', 'Gonzales', 'San Ysidro', 'Novato', \
        'Gilroy', 'Vernalis', 'Turlock', 'Beverly Hills', 'Escondido', 'South Dos Palos', \
        'San Jose', 'El Monte', 'La Habra', 'San Francisco', 'Essex', 'Fresno', 'Encino', \
        'Bellflower', 'Sonora', 'Long Beach', 'Herlong', 'Petaluma', 'Mojave', 'Callahan', \
        'Bodega', 'Denair', 'Alderpoint', 'Lomita', 'Orangevale', 'Greenville', 'Fort Bragg', \
        'Mecca', 'Torrance', 'Victorville', 'Santa Barbara', 'Guinda', 'Fort Irwin', 'Palomar Mountain', \
        'Sacramento', 'Anza', 'Bell', 'Azusa', 'Leggett', 'Hornitos', 'Thermal', 'Lafayette', 'Alameda', \
        'Herald', 'Benicia', 'Anderson', 'Riverside', 'Bakersfield', 'Taylorsville', 'Etna', 'Willows', \
        'Mather', 'Fairfax', 'Hydesville', 'Graton', 'Shafter', 'San Simeon', 'Castro Valley', 'Ranchita', \
        'Rancho Cordova', 'Wasco', 'Pasadena', 'Oak Run', 'Irvine', 'North Hollywood', 'Newhall', \
        'Murphys', 'Ferndale', 'Temecula', 'Wilton', 'White Water', 'Aguanga', 'Alviso', \
        'Rancho Cucamonga', 'Round Mountain', 'Orleans', 'Monte Rio', 'Chino Hills', \
        'Redwood City', 'Branscomb', 'Buena Park', 'Elverta', 'North Hills', 'Milpitas', \
        'West Hollywood', 'Norco', 'Half Moon Bay', 'Dos Rios', 'Yermo', 'Covina', 'Mountain View', \
        'Kingsburg', 'Carmel Valley', 'Anaheim', 'Newman', 'Spreckels', 'Grenada', 'Foothill Ranch', \
        'Palm Desert', 'Chowchilla', 'Morgan Hill', 'Orange', 'Cutler', 'Mission Viejo', 'Newport Beach', \
        'North Palm Springs', 'Shingle Springs', 'Altadena', 'Sheep Ranch', 'Livermore', 'Cressey', \
        'Forks Of Salmon', 'Loomis', 'Redding', 'Clearlake Oaks', 'Felton', 'Alta', 'Los Molinos', \
        'Brawley', 'Klamath', 'Jolon', 'Clearlake', 'Claremont', 'Soquel', 'Castaic', 'Agoura Hills', \
        'Forbestown', 'Wilseyville', 'Junction City', 'Port Hueneme', 'Lawndale', 'Acampo', 'Angwin', \
        'Glendale', 'Plymouth', 'Parker Dam', 'Zenia', 'Hayward', 'Stanford', 'Encinitas', 'Whittier', \
        'Rosemead', 'Angelus Oaks', 'Concord', 'Fawnskin', 'La Palma', 'French Gulch', 'Woodbridge', \
        'Pioneertown', 'Berkeley', 'Richgrove', 'Oakley', 'Campbell', 'Winnetka', 'San Jacinto', \
        'San Lorenzo', 'Vallecito', 'Boulder Creek', 'Oregon House', 'Shoshone', 'Palermo', 'Happy Camp', \
        'Friant', 'San Joaquin', 'Groveland', 'Imperial', 'San Miguel', 'Palos Verdes Peninsula', 'Wendel', \
        'Seal Beach', 'Montara', 'La Grange', 'Madera', 'Phillipsville', 'Forest Knolls', 'Yorkville', \
        'Ladera Ranch', 'Redlands', 'Santa Ynez', 'Pinon Hills', 'Inglewood', 'Emeryville', \
        'Sequoia National Park', 'Pacoima', 'Canby', 'Lake Forest', 'Corona', 'South Gate', \
        'Rancho Santa Margarita', 'Shaver Lake', 'Lakeshore', 'Hinkley', 'Cantua Creek', 'El Sobrante', \
        'Lynwood', 'Mentone', 'Ivanhoe', 'Nice', 'Guatay', 'Rohnert Park', 'Cedar Glen', 'Descanso', \
        'Tecate', 'San Marcos', 'Palo Cedro', 'Baldwin Park', 'Harbor City', 'Richmond', 'Meadow Vista', \
        'Soledad', 'Elk Grove', 'Gold Run', 'Forestville', 'Richvale', 'Riverbank', 'Biggs', 'Nicasio', \
        'Camp Nelson', 'Valley Village', 'Topanga', 'Chico', 'La Quinta', 'Salinas', 'Creston', 'Oakhurst',\
        'Castroville', 'Lockwood', 'Ventura', 'San Dimas', 'Huntington Beach', 'Dana Point', 'Colfax', \
        'Vacaville', 'Corcoran', 'Loma Linda', 'Orick', 'Pomona', 'Sunnyvale', 'Samoa', 'Pacific Palisades', \
        'Arcata', 'Valley Ford', 'Tujunga', 'Cerritos', 'Lathrop', 'Point Arena', 'Coronado', 'Pebble Beach', \
        'Belvedere Tiburon', 'Placerville', 'Manchester', 'Pioneer', 'Boulevard', 'Rescue', 'Burbank', \
        'Greenwood', 'San Pedro', 'Delhi', 'Stevenson Ranch', 'Cypress', 'Deer Park', 'Mariposa', 'Weott', \
        'Farmersville', 'Cloverdale', 'Bodfish', 'Aptos', 'Campo Seco', 'Menifee', 'Dunlap', 'Stevinson', \
        'Westminster', 'Big Bend', 'Westmorland', 'Menlo Park', 'San Pablo', 'Compton', 'Poway', \
        'Port Costa', 'Marysville', 'Millbrae', 'Tustin', 'Banning', 'Glen Ellen', 'Walnut Creek', \
        'Keene', 'Carmel', 'Somes Bar', 'Sultana', 'Fountain Valley', 'Homewood', 'Amboy', \
        'Thousand Palms', 'Riverdale', 'West Covina', 'Castella', 'Covelo', 'Live Oak', 'Birds Landing', \
        'Hickman', 'Granada Hills', 'Milford', 'El Centro', 'Camptonville', 'Hat Creek', 'Baker', \
        'Three Rivers', 'El Portal', 'Porterville', 'Littlerock', 'Gualala', 'Camino', 'Arbuckle', \
        'Sutter', 'Sylmar', 'Cupertino', 'San Rafael', 'Woodland', 'California City', 'Lakewood', \
        'Mammoth Lakes', 'Elk Creek', 'Catheys Valley', 'North Fork', 'Somis', 'Canoga Park', \
        'Murrieta', 'Orinda', 'San Juan Bautista', 'Thousand Oaks', 'Culver City', 'Tehachapi', \
        'Ben Lomond', 'Santa Maria', 'Death Valley', 'Rio Dell', 'Suisun City', 'Dixon', \
        'Mckinleyville', 'Kings Beach', 'Brea', 'Meridian', 'Sun City', 'Kernville', 'Fairfield', \
        'Tahoe Vista', 'Orosi', 'Artesia', 'West Sacramento', 'Bloomington', 'Eureka', 'Coleville', \
        'Big Pine', 'Hawaiian Gardens', 'Olancha', 'Hercules', 'Tomales', 'Sloughhouse', 'El Cajon', \
        'Vallejo', 'La Jolla', 'Alleghany', 'Greenview', 'Soda Springs', 'Dublin', 'Mount Hamilton', \
        'Lebec', 'Chilcoot', 'Gasquet', 'El Cerrito', 'Jamestown', 'Caspar', 'Gerber', 'Martinez', \
        'Mc Kittrick', 'San Leandro', 'Sutter Creek', 'San Carlos', 'Guadalupe', 'Winterhaven', \
        'Hemet', 'Potrero', 'Duarte', 'Stirling City', 'Fontana', 'La Verne', 'Chula Vista', \
        'Independence', 'Ballico', 'Mad River', 'Coachella', 'South Pasadena', 'Barstow', 'Tulare', \
        'Fullerton', 'Tollhouse', 'Five Points', 'Rancho Palos Verdes', 'Sonoma', 'Dulzura', 'Kyburz', \
        'Yorba Linda', 'Grizzly Flats', 'Rancho Santa Fe', 'Yucca Valley', 'Citrus Heights', 'Alpine', \
        'Reedley', 'Danville', 'Trabuco Canyon', 'San Bruno', 'Paramount', 'Winters', 'Mill Creek', \
        'Salida', 'Pine Valley', 'Hume', 'Amador City', 'Jenner', 'Lakeside', 'Ceres', 'Bridgeville', \
        'Playa Del Rey', 'Keeler', 'Seaside', 'Huron', 'Linden', 'Acton', 'Newark', 'Sierra City', \
        'Windsor', 'Travis Afb', 'Davis', 'Scott Bar', 'Freedom', 'Blairsden Graeagle', 'Lincoln', \
        'Ravendale', 'Whitmore', 'Grover Beach', 'Del Mar', 'Auburn', 'Rio Vista', 'Armona', \
        'Mira Loma', 'Sunol', 'Wishon', 'Courtland', 'O Neals', 'Rodeo', 'Blue Lake', 'Rosamond', \
        'Van Nuys', 'Trinidad', 'Pittsburg', 'Palm Springs', 'Colton', 'Caruthers', \
        'March Air Reserve Base', 'Apple Valley', 'Hughson', 'Rio Linda', 'Daly City', \
        'Canyon Dam', 'Niland', 'French Camp', 'Yuba City', 'Ontario', 'Bethel Island', \
        'Clements', 'Strathmore', 'Nevada City', 'Larkspur', 'Taft', 'Moss Landing', \
        'Arcadia', 'Meadow Valley', 'Manteca', 'Fall River Mills', 'Mount Shasta', \
        'Carson', 'Sunset Beach', 'Reseda', 'Los Osos', 'King City', 'Oceanside', \
        'Idyllwild', 'Klamath River', 'Santa Ysabel', 'Livingston', 'Los Alamos', \
        'San Clemente', 'Folsom', 'Sunland', 'Granite Bay', 'Moreno Valley', 'San Ramon',\
         'South El Monte', 'Greenbrae', 'Cazadero', 'Yucaipa', 'Saratoga', 'Summerland', \
        'Maywood', 'Le Grand', 'Capay', 'Nubieber', 'Rio Nido', 'Manhattan Beach', 'Loyalton',\
        'Oroville', 'Pinole', 'Monterey', 'Campo', 'Fowler', 'Lookout', 'Hopland', 'Topaz', \
        'Spring Valley', 'Beale Afb', 'Moraga', 'Mokelumne Hill', 'Lotus', 'Hanford', 'Los Banos', \
        'Carmichael', 'Loma Mar', 'Fish Camp', 'Carlsbad', 'Weldon', 'Bodega Bay', 'Bass Lake', \
        'Mountain Ranch', 'Springville', 'Esparto', 'Markleeville', 'South San Francisco', 'Westport',\
        'Davis Creek', 'Cottonwood', 'Chatsworth', 'La Crescenta', 'Indian Wells', 'Hilmar', \
        'Paradise', 'Cabazon', 'Winchester', 'Willow Creek', 'Llano', 'Petrolia', 'Sierra Madre', \
        'Chualar', 'Applegate', 'Bayside', 'Fields Landing', 'Tarzana', 'Santa Fe Springs', \
        'Columbia', 'Helendale', 'Rialto', 'Tranquillity', 'Brooks', 'Goodyears Bar', 'Capitola', \
        'San Gabriel', 'Cayucos', 'Shingletown', 'Tahoe City', 'Avery', 'Earp', 'Coalinga', 'Vina', \
        'Lagunitas', 'Stonyford', 'Flournoy', 'Rough And Ready', 'New Cuyama', 'Union City', 'Bishop', \
        'Arroyo Grande', 'Shasta', 'Bella Vista', 'Galt', 'Nipomo', 'Lake Hughes', 'Canyon Country', \
        'Edwards', 'Norwalk', 'Jacumba', 'Glendora', 'Pleasanton', 'Arvin', 'Westwood', 'Jackson', \
        'Calimesa', 'Weaverville', 'Eldridge', 'Little River', 'Upper Lake', 'Laguna Beach', \
        'Old Station', 'Portola Valley', 'Stinson Beach', 'Pacific Grove', 'Placentia', 'Orange Cove', \
        'Olivehurst', 'Isleton', 'Rancho Mirage', 'San Luis Obispo', 'Angels Camp', 'Silverado', \
        'Watsonville', 'San Martin', 'Saint Helena', 'Frazier Park', 'Corning', 'Palo Alto', \
        'Fellows', 'Weed', 'Modesto', 'Kirkwood', 'Knights Landing', 'Wallace', 'Twentynine Palms', \
        'Point Reyes Station', 'Piru', 'Elk', 'Penryn', 'Lockeford', 'Rocklin', 'Clayton', \
        'Kettleman City', 'Lewiston', 'Los Altos', 'Hathaway Pines', 'Montrose', 'Lytle Creek', \
        'Washington', 'San Marino', 'Raymond', 'Clipper Mills', 'San Quentin', 'Auberry', \
        'South Lake Tahoe', 'Warner Springs', 'Selma', 'Alturas', 'Sierraville', 'Yountville', \
        'Newcastle', 'Redondo Beach', 'Mount Laguna', 'Hermosa Beach', 'Midpines', 'Termo', \
        'Firebaugh', 'Shasta Lake', 'Hesperia', 'Boron', 'Marina Del Rey', 'Northridge', \
        'Blocksburg', 'Millville', 'Helm', 'Grand Terrace', 'Maxwell', 'Newport Coast', 'Comptche', \
        'Twain Harte', 'Malibu', 'Oro Grande', 'Lee Vining', 'Hyampom', 'El Dorado', 'Mount Hermon', \
        'Buttonwillow', 'Laton', 'Mc Farland', 'Boonville', 'Bolinas', 'Crescent Mills', 'Exeter', \
        'Pixley', 'Simi Valley', 'Igo', 'Antioch', 'Diamond Bar', 'Lakeport', 'La Canada Flintridge', \
        'Durham', 'Ukiah', 'Macdoel', 'Duncans Mills', 'Burney', 'Avenal', 'Ocotillo', 'Trinity Center',\
        'Mcarthur', 'Walnut', 'Lemoore', 'Burson', 'Villa Park', 'Red Bluff', 'Redway', \
        'Sun Valley', 'Copperopolis', 'Huntington Park', 'Greenfield', 'Valencia', \
        'North San Juan', 'Ripon', 'San Gregorio', 'Brownsville', 'Inverness', 'Waterford', \
        'Paso Robles', 'Paynes Creek', 'Big Bar', 'Pala', 'Lucerne Valley', 'Carlotta', \
        'Benton', 'Lamont', 'Rowland Heights', 'Patterson', 'Seiad Valley', 'Pearblossom',\
        'Cobb', 'Phelan', 'Garberville', 'Paskenta', 'Doyle', 'Glennville', 'Twin Bridges', \
        'Dobbins', 'Joshua Tree', 'Alamo', 'Monrovia', 'Chino', 'Princeton', 'Brookdale',\
         'Newbury Park', 'Grimes', 'Sugarloaf', 'Vista', 'Marina', 'Willits', 'Mill Valley', \
        'Penn Valley', 'Blythe', 'Laguna Hills', 'Pleasant Grove', 'Big Bear City', 'Calipatria',\
         'Hawthorne', 'Dos Palos', 'Orland', 'Pismo Beach', 'Stratford', 'Marshall', 'Mt Baldy', \
        'Escalon', 'Ludlow', 'Pauma Valley', 'Brentwood', 'Albion', 'Cathedral City', 'Wildomar', \
        'Fiddletown', 'Crestline', 'Nuevo', 'Lost Hills', 'National City', 'La Honda', 'Tehama', \
        'Coulterville', 'Douglas City', 'Redcrest', 'Dunnigan', 'Scotia', 'Aliso Viejo', \
        'Hacienda Heights', 'Solana Beach', 'Fair Oaks', 'Potter Valley', 'Garden Valley', \
        'Atherton', 'Byron', 'West Hills', 'Carnelian Bay', 'Tupman', 'San Geronimo', 'Bieber', \
        'Fort Bidwell', 'Rio Oso', 'Merced', 'Williams', 'Traver', 'Stanton', 'Coarsegold', \
        'Hood', 'Strawberry Valley', 'Foresthill', 'Walnut Grove', 'Sanger', 'Holtville', \
        'Glencoe', 'Dillon Beach', 'Platina', 'Philo', 'Green Valley Lake', 'Gridley', \
        'Imperial Beach', 'Litchfield', 'Desert Center', 'Pinecrest', 'Dorris', 'Myers Flat', \
        'Crows Landing', 'Eagleville', 'Adelanto', 'Heber', 'Mineral', 'Pico Rivera', 'Elmira', \
        'Burlingame', 'Cassel', 'Porter Ranch', 'Long Barn', 'Gustine', 'Paicines', 'El Nido', \
        'Arnold', 'Manton', 'Shandon', 'Echo Lake', 'Homeland', 'Cool', 'Ducor', 'Montclair', \
        'Seeley', 'Bonsall', 'Calpine', 'Pleasant Hill', 'Lower Lake', 'Avila Beach', 'Occidental', \
        'Adin', 'Forest Ranch', 'Planada', 'Pine Grove', 'Navarro', 'Belmont', 'Raisin City', \
        'Goleta', 'Witter Springs', 'Madeline', 'Cardiff By The Sea', 'Atwater', 'Bradley', \
        'Forest Falls', 'Morro Bay', 'Caliente', 'Landers', 'Dinuba', 'Nicolaus', 'Likely', \
        'Lake Isabella', 'Biola', 'Piercy', 'Big Bear Lake', 'Redwood Valley', 'Running Springs',\
         'Crockett', 'Sausalito', 'Magalia', 'Yreka', 'Honeydew', 'Standish', 'Grass Valley', \
        'Diamond Springs', 'Westlake Village', 'Brisbane', 'Keyes', 'Wrightwood', 'El Segundo', \
        'Atascadero', 'Corona Del Mar', 'Tahoma', 'Susanville', 'Laguna Niguel', 'Studio City', \
        'The Sea Ranch', 'Posey', 'Valley Springs', 'Pollock Pines', 'Montebello', 'Salyer', \
        'Miranda', 'Twain', 'San Ardo', 'Antelope', 'Smith River', 'Lucerne', 'Janesville', \
        'Earlimart', 'Santee', 'Salton City', 'Santa Paula', 'Fillmore', 'Pope Valley', \
        'Bridgeport', 'Calabasas', 'Kenwood', 'Jamul', 'River Pines', 'Big Creek', 'Surfside', \
        'Avalon', 'Corte Madera', 'Templeton', 'Roseville', 'Winton', 'Lemon Grove', 'Weimar', \
        'Browns Valley', 'Kneeland', 'Lake Arrowhead', 'Woody', 'Korbel', 'Solvang', 'Quincy', \
        'Bonita', 'Fortuna', 'Casmalia', 'Miramonte', 'Dunsmuir', 'Mi Wuk Village', 'Smartville', \
        'Costa Mesa', 'Guerneville', 'San Fernando', 'Tracy', 'Nipton', 'Cedarville', \
        'Los Alamitos', 'Albany', 'Emigrant Gap', 'Loleta', 'Pacifica', 'Terra Bella', \
        'Oak View', 'Annapolis', 'Woodacre', 'Davenport', 'Valley Center', 'Beaumont', \
        'Cotati', 'Carmel By The Sea', 'Hornbrook', 'Oakdale', 'Temple City', 'Glenn', \
        'Penngrove', 'Scotts Valley', 'Snelling', 'Bangor', 'Somerset', 'Sebastopol', \
        'Needles', 'Capistrano Beach', 'Volcano', 'Kerman', 'Soulsbyville', 'Hamilton City', \
        'Middletown', 'Dutch Flat', 'Mccloud', 'Oak Park', 'Gazelle', 'San Andreas', \
        'Squaw Valley', 'Lemon Cove', 'Laytonville', 'Mendocino', 'Julian', 'Lakehead', \
        'Lindsay', 'San Juan Capistrano', 'June Lake', 'Olympic Valley', 'Geyserville', \
        'Portola', 'Santa Clarita', 'Venice', 'Chester', 'Mountain Center', 'Olema', \
        'Carpinteria', 'Highland', 'Wheatland', 'Madison', 'Johannesburg', 'Buellton', \
        'California Hot Springs', 'Delano', 'Healdsburg', 'Moorpark', 'Georgetown', \
        'Butte City', 'Prather', 'Kelseyville', 'Borrego Springs', 'Daggett', 'Downieville', \
        'Ramona', 'Montgomery Creek', 'San Lucas', 'Wofford Heights']
    
    return sorted(cities)
