from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.db import models

CLOTHING_TYPE_CHOICES = \
    [('Streetwear Style', 'Streetwear Style'), ('Ethnic fashion style ', 'Ethnic fashion style '),
     ('Formal Office Wear', 'Formal Office Wear'), ('Business Casual', 'Business Casual'),
     ('Evening Black Tie', 'Evening Black Tie'), ('Sports Wear', 'Sports Wear'),
     ('Girly Style ', 'Girly Style '), ('Androgynous fashion style', 'Androgynous fashion style'),
     ('E girl', 'E girl'), ('Scene fashion style', 'Scene fashion style'),
     ('Rocker Chic Style', 'Rocker Chic Style'), ('Skateboarders', 'Skateboarders'),
     ('Goth Fashion', 'Goth Fashion'), ('Maternity Style', 'Maternity Style'),
     ('Lolita Fashion', 'Lolita Fashion'), ('Gothic lolita style', 'Gothic lolita style'),
     ('Hip Hop Style', 'Hip Hop Style'), ('Chave culture Style', 'Chave culture Style'),
     ('Kawaii fashion', 'Kawaii fashion'), ('Preppy style', 'Preppy style'),
     ('Cowgirl fashion style', 'Cowgirl fashion style'),
     ('Lagenlook Fashion style', 'Lagenlook Fashion style'),
     ('Girl next door fashion style', 'Girl next door fashion style'),
     ('Casual Chic Style', 'Casual Chic Style'), ('Geeky chic Style', 'Geeky chic Style'),
     ('Military style', 'Military style'), ('Retro Fashion', 'Retro Fashion'),
     ('Flapper fashion (20s look),', 'Flapper fashion (20s look),'),
     ('Tomboy', 'Tomboy'), ('Garconne look', 'Garconne look'),
     ('Vacation (Resort), style', 'Vacation (Resort), style'), ('Camp Style', 'Camp Style'),
     ('Artsy Fashion style', 'Artsy Fashion style'), ('Grunge style', 'Grunge style'),
     ('Punk', 'Punk'), ('Boho/Bohemian chic', 'Boho/Bohemian chic'),
     ('Biker fashion', 'Biker fashion'), ('Psychedelic Fashion style', 'Psychedelic Fashion style'),
     ('Cosplay Fashion', 'Cosplay Fashion'), ('Haute Couture', 'Haute Couture'),
     ('Modest fashion', 'Modest fashion'), ('Prairie chic style', 'Prairie chic style'),
     ('Rave fashion', 'Rave fashion'), ('Flamboyant style', 'Flamboyant style'),
     ('Ankara Fashion Style', 'Ankara Fashion Style'),
     ('Arthoe Fashion Style', 'Arthoe Fashion Style')]

CLOTHING_METRIALS_TYPE_CHOICES = \
    [('Abaca', 'Abaca'), ('Aba', 'Aba'), ('Acetate ', 'Acetate '),
     ('Acrylic fabric', 'Acrylic fabric'),
     ('Active Comfort Denim', 'Active Comfort Denim'),
     ('Admiralty cloth', 'Admiralty cloth'), ('Aerophane', 'Aerophane'),
     ('Aertex', 'Aertex'), ('Aida Canvas / Aida cloth', 'Aida Canvas / Aida cloth'),
     ('Airplane cloth', 'Airplane cloth'), ('Albert Cloth', 'Albert Cloth'),
     ('Albatross', 'Albatross'), ('Alepine', 'Alepine'), ('Alpaca', 'Alpaca'),
     ('Alpaca crepe', 'Alpaca crepe'), ('American Pima Cotton', 'American Pima Cotton'),
     ('Angora fibres', 'Angora fibres'), ('Angola', 'Angola'), ('Anti-pill', 'Anti-pill'),
     ('Antique satin', 'Antique satin'), (' Ardass', ' Ardass'), ('Argyle', 'Argyle'),
     ('Armure', 'Armure'), ('Art Linen', 'Art Linen'), ('Astrakhan', 'Astrakhan'),
     ('Atlas', 'Atlas'), ('Awnings', 'Awnings'),
     ('Baby Combing Wool', 'Baby Combing Wool'), ('Baft', 'Baft'),
     ('Bagheera Velvet', 'Bagheera Velvet'), ('Ballistic', 'Ballistic'),
     ('Balloon cloth', 'Balloon cloth'), ('Banbury plush', 'Banbury plush'),
     ('Bamboo fibers', 'Bamboo fibers'), ('Banana Fabric', 'Banana Fabric'),
     ('Bandana', 'Bandana'), ('Baize', 'Baize'), ('Bark Cloth', 'Bark Cloth'),
     ('Baronet satin', 'Baronet satin'), ('Basket weave', 'Basket weave'),
     ('Bathroom Blanketing (Blanket cloth)', 'Bathroom Blanketing (Blanket cloth)'),
     ('Batik', 'Batik'), ('Batiste', 'Batiste'), ('Batt or Batting', 'Batt or Batting'),
     ('Beaded', 'Beaded'), ('Beaver cloth', 'Beaver cloth'), ('Belly Wool', 'Belly Wool'),
     ('Bemberg', 'Bemberg'), ('Bengaline /Faille', 'Bengaline /Faille'),
     ('Binding cloth', 'Binding cloth'), ('Blanket cloth', 'Blanket cloth'),
     ('Bobbinet', 'Bobbinet'), ('Bombazine', 'Bombazine'), ('Bunting', 'Bunting'),
     ('Burlap', 'Burlap'), ('Bedford (Cord)', 'Bedford (Cord)'),
     ('Berber fleece', 'Berber fleece'),
     ('Bicast leather (PU leather)', 'Bicast leather (PU leather)'),
     ('Biopolished cotton', 'Biopolished cotton'), ('Black Wool', 'Black Wool'),
     ('Blends', 'Blends'), ('Bonded leather', 'Bonded leather'),
     ('Bombazine', 'Bombazine'), ('Boiled Wool', 'Boiled Wool'),
     ('Botany Wools', 'Botany Wools'), ('Boynge', 'Boynge'),
     ('Breech or Britch Wool', 'Breech or Britch Wool'), ('Brocade', 'Brocade'),
     ('Broderie Anglaise', 'Broderie Anglaise'), ('Brocatelle', 'Brocatelle'),
     ('Brushed Wool', 'Brushed Wool'), ('Buck Fleece', 'Buck Fleece'),
     ('Burlap', 'Burlap'), ('Calico', 'Calico'), ('Cambric', 'Cambric'),
     ('Camel’s Hair', 'Camel’s Hair'), ('Camlet', 'Camlet'),
     ('Canton crepe', 'Canton crepe'), ('Canvas', 'Canvas'), ('Casement', 'Casement'),
     ('Cashmere', 'Cashmere'), ('Carpet Wool', 'Carpet Wool'), ('Cashgora', 'Cashgora'),
     ('Cashmerlon', 'Cashmerlon'), ('Cerecloth / altar cloth', 'Cerecloth / altar cloth'),
     ('Cavalry Twill', 'Cavalry Twill'), ('Challis', 'Challis'),
     ('Chambray / Chambric', 'Chambray / Chambric'), ('Charmeuse', 'Charmeuse'),
     ('Chamoise', 'Chamoise'), ('Chantilly lace', 'Chantilly lace'),
     ('Charvet silk', 'Charvet silk'), ('Chanel tweed', 'Chanel tweed'),
     ('Checks', 'Checks'), ('Cheese cloth', 'Cheese cloth'), ('Chenille', 'Chenille'),
     ('Cheviot', 'Cheviot'), ('Chevron', 'Chevron'), ('Chiffon', 'Chiffon'),
     ('China silk ', 'China silk '), ('Chinchilla cloth', 'Chinchilla cloth'),
     ('Chint', 'Chint'), ('Chino', 'Chino'), ('Chintz', 'Chintz'), ('Chite', 'Chite'),
     ('Chire', 'Chire'), ('Cisele velvet', 'Cisele velvet'), ('Cloque', 'Cloque'),
     ('Coating', 'Coating'), ('Colorfast', 'Colorfast'),
     ('Combed cotton', 'Combed cotton'), ('Corduroy', 'Corduroy'),
     ('Cottagora', 'Cottagora'), ('Cotton', 'Cotton'), (
         'Types of cotton fabric and cotton weave ',
         'Types of cotton fabric and cotton weave '),
     ('Cotton backed Satin', 'Cotton backed Satin'), ('Cotton voile', 'Cotton voile'),
     ('Cotton Lawn', 'Cotton Lawn'), ('Crazy Horse', 'Crazy Horse'),
     ('Crochet', 'Crochet'), ('Crepe', 'Crepe'), ('Crepe back satin', 'Crepe back satin'),
     ('Cretonne', 'Cretonne'), ('Crepe de chine', 'Crepe de chine'),
     ('Crinkle satin', 'Crinkle satin'), ('Crinoline ', 'Crinoline '),
     ('Crinoline net', 'Crinoline net'), ('Cupro', 'Cupro'), ('Dacron', 'Dacron'),
     ('Duplex prints', 'Duplex prints'), ('Damask', 'Damask'), ('Dazzle', 'Dazzle'),
     ('Deerskin', 'Deerskin'), ('Denim / dungaree / jean', 'Denim / dungaree / jean'),
     ('Diaper cloth', 'Diaper cloth'), ('Dimity', 'Dimity'), ('Doeskin', 'Doeskin'),
     ('Dommet flannel', 'Dommet flannel'), ('Donegal', 'Donegal'), ('Dorian', 'Dorian'),
     ('Dotted Swiss', 'Dotted Swiss'), ('Double cloth', 'Double cloth'),
     ('Double Gauze', 'Double Gauze'), ('Double knit', 'Double knit'), ('Down', 'Down'),
     ('Dress net', 'Dress net'), ('Drill', 'Drill'), ('Duchess satin', 'Duchess satin'),
     ('Duck cloth', 'Duck cloth'), ('Duvetyne', 'Duvetyne'), ('Duffel', 'Duffel'),
     ('Dupioni', 'Dupioni'), ('Egyptian cotton', 'Egyptian cotton'),
     ('Epyngle', 'Epyngle'), ('Eyelet', 'Eyelet'), ('Eyelash', 'Eyelash'),
     ('Elastane', 'Elastane'), ('Elastique', 'Elastique'),
     ('Embroidered fabric', 'Embroidered fabric'), ('Eolienne', 'Eolienne'),
     ('English net', 'English net'), ('Faconne', 'Faconne'), ('Faille', 'Faille'),
     ('Fake fur', 'Fake fur'), ('Feathers', 'Feathers'), ('Faux leather', 'Faux leather'),
     ('Felt', 'Felt'), ('Flannel', 'Flannel'), ('Flanellette', 'Flanellette'),
     ('Flax', 'Flax'), ('Foulard', 'Foulard'), ('French terry', 'French terry'),
     ('Frieze', 'Frieze'), ('Full-grain leather', 'Full-grain leather'),
     ('Faux Fur', 'Faux Fur'), ('Faux silk', 'Faux silk'), ('Frieze', 'Frieze'),
     ('Fustian', 'Fustian'), ('Fur', 'Fur'), ('Gabardine', 'Gabardine'),
     ('Gauze', 'Gauze'), ('Georgette', 'Georgette'), ('Gingham', 'Gingham'),
     ('Glen checks', 'Glen checks'), ('Gossamer', 'Gossamer'), ('Grosgrain', 'Grosgrain'),
     ('Handkerchief Linen', 'Handkerchief Linen'), ('Habutai', 'Habutai'),
     ('Haircloth', 'Haircloth'), ('Hessian', 'Hessian'), ('Hemp', 'Hemp'),
     ('Homespun', 'Homespun'), ('Hopsacking', 'Hopsacking'), ('Huckaback', 'Huckaback'),
     ('Ikat', 'Ikat'), ('Illusion', 'Illusion'), ('Interlock', 'Interlock'),
     ('Irish poplin', 'Irish poplin'), ('Jaconet', 'Jaconet'), ('Jacquard', 'Jacquard'),
     ('Jersey', 'Jersey'), ('Jute', 'Jute'), ('Khakhi', 'Khakhi'), ('Kidskin', 'Kidskin'),
     ('Knit', 'Knit'), ('Types of knit', 'Types of knit'),
     ('Knitted fabric ', 'Knitted fabric '), ('Lace', 'Lace'),
     ('Lamb’s wool', 'Lamb’s wool'), ('Lambskin', 'Lambskin'), ('Layette', 'Layette'),
     ('Linen', 'Linen'), ('Different linen fabric', 'Different linen fabric'),
     ('Linsey woolsey', 'Linsey woolsey'), ('Lint', 'Lint'), ('Lisle', 'Lisle'),
     ('Llama', 'Llama'), ('Loden Fabric', 'Loden Fabric'), ('Lycra', 'Lycra'),
     ('Lurex', 'Lurex'), ('Leather', 'Leather'), ('Leathertte', 'Leathertte'),
     ('Liquid cotton', 'Liquid cotton'), ('Lycra', 'Lycra'), ('Macrame', 'Macrame'),
     ('Macinaw', 'Macinaw'), ('Mackinosh', 'Mackinosh'), ('Madras', 'Madras'),
     ('Marled', 'Marled'), ('Marquissette', 'Marquissette'), ('Marvello', 'Marvello'),
     ('Marceline', 'Marceline'), ('Matelasse', 'Matelasse'),
     ('Matte fabric', 'Matte fabric'), ('Melange', 'Melange'),
     ('Merino  wool', 'Merino  wool'), ('Messaline', 'Messaline'), ('Mesh', 'Mesh'),
     ('Melton', 'Melton'), ('Microfiber', 'Microfiber'), ('Milanese', 'Milanese'),
     ('Milk yarn', 'Milk yarn'), ('Modal', 'Modal'), ('Moire', 'Moire'),
     ('Mohair', 'Mohair'), ('Moleskin', 'Moleskin'), ('Monks cloth', 'Monks cloth'),
     ('Moss crepe', 'Moss crepe'), ('Mother of pearl', 'Mother of pearl'),
     ('Mull', 'Mull'), ('Muslin', 'Muslin'), ('Nankeen', 'Nankeen'),
     ('Nappa Leather', 'Nappa Leather'), ('Neoprene', 'Neoprene'), ('Nep', 'Nep'),
     ('Netting', 'Netting'), ('Net fabric', 'Net fabric'), ('Ninon', 'Ninon'),
     ('Nonwoven fabric', 'Nonwoven fabric'), ('Nubuck', 'Nubuck'), ('Nylon', 'Nylon'),
     ('Nytril', 'Nytril'), ('Oilcloth', 'Oilcloth'), ('Olefin', 'Olefin'),
     ('Organdie / Organdy', 'Organdie / Organdy'), ('Organic cotton', 'Organic cotton'),
     ('Organza', 'Organza'), ('Ottoman rib', 'Ottoman rib'), ('Oilcloth', 'Oilcloth'),
     ('Outing Flannel', 'Outing Flannel'), ('Oxford cloth', 'Oxford cloth'),
     ('Paisley', 'Paisley'), ('Panama cloth', 'Panama cloth'), ('Panne', 'Panne'),
     ('Pashmina', 'Pashmina'), ('Patent Leather', 'Patent Leather'),
     ('Peached fabric', 'Peached fabric'), ('Pearlized fabric', 'Pearlized fabric'),
     ('Percale', 'Percale'), ('Performance Knit', 'Performance Knit'),
     ('Permanent press fabric', 'Permanent press fabric'),
     ('Peau de Soie', 'Peau de Soie'), ('Petersham', 'Petersham'),
     ('Pile knit', 'Pile knit'), ('Pile weave', 'Pile weave'), ('Pill', 'Pill'),
     ('Pilot cloth', 'Pilot cloth'), ('Pima cotton', 'Pima cotton'),
     ('Pincord', 'Pincord'), ('Pinpoint', 'Pinpoint'),
     ('Pina Fabric (Pineapple)', 'Pina Fabric (Pineapple)'), ('Pinstripe', 'Pinstripe'),
     ('Pique', 'Pique'), ('Plisse', 'Plisse'), ('Plush', 'Plush'),
     ('Point d’esprit', 'Point d’esprit'), ('Pointelle', 'Pointelle'),
     ('Poiret', 'Poiret'), ('Pongee silk', 'Pongee silk'),
     ('Poodle cloth', 'Poodle cloth'), ('Polo cloth', 'Polo cloth'),
     ('Polished cotton', 'Polished cotton'), ('Polyester', 'Polyester'),
     ('Polyethylene', 'Polyethylene'), ('Polypropylene', 'Polypropylene'),
     ('Polyresin', 'Polyresin'), ('Polystyrene', 'Polystyrene'),
     ('Ponte Roma', 'Ponte Roma'), ('Poplin', 'Poplin'), ('Poult de soi', 'Poult de soi'),
     ('Quilted fabric', 'Quilted fabric'), ('Rabbit hair/wool', 'Rabbit hair/wool'),
     ('Raccoon fur', 'Raccoon fur'), ('Radium', 'Radium'), ('Raffia', 'Raffia'),
     ('Ramie', 'Ramie'), ('Raschel knit', 'Raschel knit'), ('Rayon', 'Rayon'),
     ('Rayon Spandex', 'Rayon Spandex'), ('Repp', 'Repp'), ('Resin', 'Resin'),
     ('Rib Knit', 'Rib Knit'), ('Ribbon', 'Ribbon'), ('Ric Rac', 'Ric Rac'),
     ('Ringspun fabric', 'Ringspun fabric'), ('Ripstop', 'Ripstop'), ('Russet', 'Russet'),
     ('Sailcloth', 'Sailcloth'), ('Santoprene', 'Santoprene'), ('Sarcenet', 'Sarcenet'),
     ('Sarong skirt', 'Sarong skirt'), ('Sateen', 'Sateen'), ('Satin', 'Satin'),
     ('Types of satin and satin weave', 'Types of satin and satin weave'),
     ('Scrim', 'Scrim'), ('Seersucker', 'Seersucker'), ('Serge', 'Serge'),
     ('Serpentine crepe', 'Serpentine crepe'), ('Sequin Fabric', 'Sequin Fabric'),
     ('Sharkskin', 'Sharkskin'), ('Shantung', 'Shantung'), ('Sheeting', 'Sheeting'),
     ('Sherpa (fleece)', 'Sherpa (fleece)'), ('Silesie', 'Silesie'),
     ('Silk Satin', 'Silk Satin'), ('Silk', 'Silk'),
     ('Types of silk fabric and silk weaves', 'Types of silk fabric and silk weaves'),
     ('Simplex', 'Simplex'), ('Sinamay', 'Sinamay'), ('Sisal', 'Sisal'),
     ('Slipper Satin', 'Slipper Satin'), ('Slub jersey', 'Slub jersey'),
     ('Spandex', 'Spandex'), ('Stitch bonded fabric', 'Stitch bonded fabric'),
     ('Stone washed', 'Stone washed'), ('Surah', 'Surah'), ('Suede', 'Suede'),
     ('Suedecloth', 'Suedecloth'), ('Sueded fleece', 'Sueded fleece'),
     ('Supima', 'Supima'), ('Supriva', 'Supriva'), ('Swiss Dot', 'Swiss Dot'),
     ('Synthetic', 'Synthetic'), ('Sweater knit', 'Sweater knit'), ('Tactel', 'Tactel'),
     ('Taffeta', 'Taffeta'), ('Tapa cloth', 'Tapa cloth'), ('Tape yarn', 'Tape yarn'),
     ('Tapestry', 'Tapestry'), ('Tarpaulin', 'Tarpaulin'), ('Tartan', 'Tartan'),
     ('Tattersall', 'Tattersall'), ('Teflon', 'Teflon'), ('Terrycloth', 'Terrycloth'),
     ('Terry Velvet', 'Terry Velvet'), ('Thai silk', 'Thai silk'),
     ('Thermal knit', 'Thermal knit'), ('Ticking', 'Ticking'), ('Tissue', 'Tissue'),
     ('Toweling', 'Toweling'), ('Toile', 'Toile'),
     ('Transparent Velvet', 'Transparent Velvet'), ('Tropical wool', 'Tropical wool'),
     ('Tricot', 'Tricot'), ('Tricotine', 'Tricotine'), ('Tri Acetate', 'Tri Acetate'),
     ('Tricollete', 'Tricollete'), ('Tsumugi Silk', 'Tsumugi Silk'),
     ('Tufted fabric', 'Tufted fabric'), ('Tulle', 'Tulle'),
     ('Tusseh silk / Tussah silk', 'Tusseh silk / Tussah silk'), ('Tweed', 'Tweed'),
     ('Twill', 'Twill'), ('Ultrasuede', 'Ultrasuede'), ('Velboa', 'Velboa'),
     ('Veloutine', 'Veloutine'), ('Velour', 'Velour'), ('Velvet', 'Velvet'),
     ('Velveteen', 'Velveteen'), ('Velveteen plush', 'Velveteen plush'),
     ('Venecia', 'Venecia'), ('Venetian fabric ', 'Venetian fabric '),
     ('Venice', 'Venice'), ('Vichy', 'Vichy'), ('Vicuna', 'Vicuna'), ('Vinyl', 'Vinyl'),
     ('Viscose', 'Viscose'), ('Voile', 'Voile'), ('Washable Paper', 'Washable Paper'),
     ('Wadmal', 'Wadmal'), ('Waffle cloth', 'Waffle cloth'), ('Whipcord', 'Whipcord'),
     ('Wincey', 'Wincey'), ('Wirecloth', 'Wirecloth'), ('Wool', 'Wool'),
     ('Fabrics of wool fabric and weave', 'Fabrics of wool fabric and weave'),
     ('Wool crepe', 'Wool crepe'), ('Woolsy', 'Woolsy'), ('Worsted wool', 'Worsted wool'),
     ('Worsted ', 'Worsted '), ('Worcester', 'Worcester'), ('Yak', 'Yak'),
     ('Yoryu', 'Yoryu'), ('Zanella', 'Zanella'), ('Zephyr', 'Zephyr'),
     ('Zibeline', 'Zibeline'), ('Abaca', 'Abaca'), ('Aba', 'Aba'),
     ('Acetate ', 'Acetate '), ('Acrylic fabric', 'Acrylic fabric'),
     ('Active Comfort Denim', 'Active Comfort Denim'),
     ('Admiralty cloth', 'Admiralty cloth'), ('Aerophane', 'Aerophane'),
     ('Aertex', 'Aertex'), ('Aida Canvas / Aida cloth', 'Aida Canvas / Aida cloth'),
     ('Airplane cloth', 'Airplane cloth'), ('Albert Cloth', 'Albert Cloth'),
     ('Albatross', 'Albatross'), ('Alepine', 'Alepine'), ('Alpaca', 'Alpaca'),
     ('Alpaca crepe', 'Alpaca crepe'), ('American Pima Cotton', 'American Pima Cotton'),
     ('Angora fibres', 'Angora fibres'), ('Angola', 'Angola'), ('Anti-pill', 'Anti-pill'),
     ('Antique satin', 'Antique satin'), (' Ardass', ' Ardass'), ('Argyle', 'Argyle'),
     ('Armure', 'Armure'), ('Art Linen', 'Art Linen'), ('Astrakhan', 'Astrakhan'),
     ('Atlas', 'Atlas'), ('Awnings', 'Awnings'),
     ('Baby Combing Wool', 'Baby Combing Wool'), ('Baft', 'Baft'),
     ('Bagheera Velvet', 'Bagheera Velvet'), ('Ballistic', 'Ballistic'),
     ('Balloon cloth', 'Balloon cloth'), ('Banbury plush', 'Banbury plush'),
     ('Bamboo fibers', 'Bamboo fibers'), ('Banana Fabric', 'Banana Fabric'),
     ('Bandana', 'Bandana'), ('Baize', 'Baize'), ('Bark Cloth', 'Bark Cloth'),
     ('Baronet satin', 'Baronet satin'), ('Basket weave', 'Basket weave'),
     ('Bathroom Blanketing (Blanket cloth)', 'Bathroom Blanketing (Blanket cloth)'),
     ('Batik', 'Batik'), ('Batiste', 'Batiste'), ('Batt or Batting', 'Batt or Batting'),
     ('Beaded', 'Beaded'), ('Beaver cloth', 'Beaver cloth'), ('Belly Wool', 'Belly Wool'),
     ('Bemberg', 'Bemberg'), ('Bengaline /Faille', 'Bengaline /Faille'),
     ('Binding cloth', 'Binding cloth'), ('Blanket cloth', 'Blanket cloth'),
     ('Bobbinet', 'Bobbinet'), ('Bombazine', 'Bombazine'), ('Bunting', 'Bunting'),
     ('Burlap', 'Burlap'), ('Bedford (Cord)', 'Bedford (Cord)'),
     ('Berber fleece', 'Berber fleece'),
     ('Bicast leather (PU leather)', 'Bicast leather (PU leather)'),
     ('Biopolished cotton', 'Biopolished cotton'), ('Black Wool', 'Black Wool'),
     ('Blends', 'Blends'), ('Bonded leather', 'Bonded leather'),
     ('Bombazine', 'Bombazine'), ('Boiled Wool', 'Boiled Wool'),
     ('Botany Wools', 'Botany Wools'), ('Boynge', 'Boynge'),
     ('Breech or Britch Wool', 'Breech or Britch Wool'), ('Brocade', 'Brocade'),
     ('Broderie Anglaise', 'Broderie Anglaise'), ('Brocatelle', 'Brocatelle'),
     ('Brushed Wool', 'Brushed Wool'), ('Buck Fleece', 'Buck Fleece'),
     ('Burlap', 'Burlap'), ('Calico', 'Calico'), ('Cambric', 'Cambric'),
     ('Camel’s Hair', 'Camel’s Hair'), ('Camlet', 'Camlet'),
     ('Canton crepe', 'Canton crepe'), ('Canvas', 'Canvas'), ('Casement', 'Casement'),
     ('Cashmere', 'Cashmere'), ('Carpet Wool', 'Carpet Wool'), ('Cashgora', 'Cashgora'),
     ('Cashmerlon', 'Cashmerlon'), ('Cerecloth / altar cloth', 'Cerecloth / altar cloth'),
     ('Cavalry Twill', 'Cavalry Twill'), ('Challis', 'Challis'),
     ('Chambray / Chambric', 'Chambray / Chambric'), ('Charmeuse', 'Charmeuse'),
     ('Chamoise', 'Chamoise'), ('Chantilly lace', 'Chantilly lace'),
     ('Charvet silk', 'Charvet silk'), ('Chanel tweed', 'Chanel tweed'),
     ('Checks', 'Checks'), ('Cheese cloth', 'Cheese cloth'), ('Chenille', 'Chenille'),
     ('Cheviot', 'Cheviot'), ('Chevron', 'Chevron'), ('Chiffon', 'Chiffon'),
     ('China silk ', 'China silk '), ('Chinchilla cloth', 'Chinchilla cloth'),
     ('Chint', 'Chint'), ('Chino', 'Chino'), ('Chintz', 'Chintz'), ('Chite', 'Chite'),
     ('Chire', 'Chire'), ('Cisele velvet', 'Cisele velvet'), ('Cloque', 'Cloque'),
     ('Coating', 'Coating'), ('Colorfast', 'Colorfast'),
     ('Combed cotton', 'Combed cotton'), ('Corduroy', 'Corduroy'),
     ('Cottagora', 'Cottagora'), ('Cotton', 'Cotton'), (
         'Types of cotton fabric and cotton weave ',
         'Types of cotton fabric and cotton weave '),
     ('Cotton backed Satin', 'Cotton backed Satin'), ('Cotton voile', 'Cotton voile'),
     ('Cotton Lawn', 'Cotton Lawn'), ('Crazy Horse', 'Crazy Horse'),
     ('Crochet', 'Crochet'), ('Crepe', 'Crepe'), ('Crepe back satin', 'Crepe back satin'),
     ('Cretonne', 'Cretonne'), ('Crepe de chine', 'Crepe de chine'),
     ('Crinkle satin', 'Crinkle satin'), ('Crinoline ', 'Crinoline '),
     ('Crinoline net', 'Crinoline net'), ('Cupro', 'Cupro'), ('Dacron', 'Dacron'),
     ('Duplex prints', 'Duplex prints'), ('Damask', 'Damask'), ('Dazzle', 'Dazzle'),
     ('Deerskin', 'Deerskin'), ('Denim / dungaree / jean', 'Denim / dungaree / jean'),
     ('Diaper cloth', 'Diaper cloth'), ('Dimity', 'Dimity'), ('Doeskin', 'Doeskin'),
     ('Dommet flannel', 'Dommet flannel'), ('Donegal', 'Donegal'), ('Dorian', 'Dorian'),
     ('Dotted Swiss', 'Dotted Swiss'), ('Double cloth', 'Double cloth'),
     ('Double Gauze', 'Double Gauze'), ('Double knit', 'Double knit'), ('Down', 'Down'),
     ('Dress net', 'Dress net'), ('Drill', 'Drill'), ('Duchess satin', 'Duchess satin'),
     ('Duck cloth', 'Duck cloth'), ('Duvetyne', 'Duvetyne'), ('Duffel', 'Duffel'),
     ('Dupioni', 'Dupioni'), ('Egyptian cotton', 'Egyptian cotton'),
     ('Epyngle', 'Epyngle'), ('Eyelet', 'Eyelet'), ('Eyelash', 'Eyelash'),
     ('Elastane', 'Elastane'), ('Elastique', 'Elastique'),
     ('Embroidered fabric', 'Embroidered fabric'), ('Eolienne', 'Eolienne'),
     ('English net', 'English net'), ('Faconne', 'Faconne'), ('Faille', 'Faille'),
     ('Fake fur', 'Fake fur'), ('Feathers', 'Feathers'), ('Faux leather', 'Faux leather'),
     ('Felt', 'Felt'), ('Flannel', 'Flannel'), ('Flanellette', 'Flanellette'),
     ('Flax', 'Flax'), ('Foulard', 'Foulard'), ('French terry', 'French terry'),
     ('Frieze', 'Frieze'), ('Full-grain leather', 'Full-grain leather'),
     ('Faux Fur', 'Faux Fur'), ('Faux silk', 'Faux silk'), ('Frieze', 'Frieze'),
     ('Fustian', 'Fustian'), ('Fur', 'Fur'), ('Gabardine', 'Gabardine'),
     ('Gauze', 'Gauze'), ('Georgette', 'Georgette'), ('Gingham', 'Gingham'),
     ('Glen checks', 'Glen checks'), ('Gossamer', 'Gossamer'), ('Grosgrain', 'Grosgrain'),
     ('Handkerchief Linen', 'Handkerchief Linen'), ('Habutai', 'Habutai'),
     ('Haircloth', 'Haircloth'), ('Hessian', 'Hessian'), ('Hemp', 'Hemp'),
     ('Homespun', 'Homespun'), ('Hopsacking', 'Hopsacking'), ('Huckaback', 'Huckaback'),
     ('Ikat', 'Ikat'), ('Illusion', 'Illusion'), ('Interlock', 'Interlock'),
     ('Irish poplin', 'Irish poplin'), ('Jaconet', 'Jaconet'), ('Jacquard', 'Jacquard'),
     ('Jersey', 'Jersey'), ('Jute', 'Jute'), ('Khakhi', 'Khakhi'), ('Kidskin', 'Kidskin'),
     ('Knit', 'Knit'), ('Types of knit', 'Types of knit'),
     ('Knitted fabric ', 'Knitted fabric '), ('Lace', 'Lace'),
     ('Lamb’s wool', 'Lamb’s wool'), ('Lambskin', 'Lambskin'), ('Layette', 'Layette'),
     ('Linen', 'Linen'), ('Different linen fabric', 'Different linen fabric'),
     ('Linsey woolsey', 'Linsey woolsey'), ('Lint', 'Lint'), ('Lisle', 'Lisle'),
     ('Llama', 'Llama'), ('Loden Fabric', 'Loden Fabric'), ('Lycra', 'Lycra'),
     ('Lurex', 'Lurex'), ('Leather', 'Leather'), ('Leathertte', 'Leathertte'),
     ('Liquid cotton', 'Liquid cotton'), ('Lycra', 'Lycra'), ('Macrame', 'Macrame'),
     ('Macinaw', 'Macinaw'), ('Mackinosh', 'Mackinosh'), ('Madras', 'Madras'),
     ('Marled', 'Marled'), ('Marquissette', 'Marquissette'), ('Marvello', 'Marvello'),
     ('Marceline', 'Marceline'), ('Matelasse', 'Matelasse'),
     ('Matte fabric', 'Matte fabric'), ('Melange', 'Melange'),
     ('Merino  wool', 'Merino  wool'), ('Messaline', 'Messaline'), ('Mesh', 'Mesh'),
     ('Melton', 'Melton'), ('Microfiber', 'Microfiber'), ('Milanese', 'Milanese'),
     ('Milk yarn', 'Milk yarn'), ('Modal', 'Modal'), ('Moire', 'Moire'),
     ('Mohair', 'Mohair'), ('Moleskin', 'Moleskin'), ('Monks cloth', 'Monks cloth'),
     ('Moss crepe', 'Moss crepe'), ('Mother of pearl', 'Mother of pearl'),
     ('Mull', 'Mull'), ('Muslin', 'Muslin'), ('Nankeen', 'Nankeen'),
     ('Nappa Leather', 'Nappa Leather'), ('Neoprene', 'Neoprene'), ('Nep', 'Nep'),
     ('Netting', 'Netting'), ('Net fabric', 'Net fabric'), ('Ninon', 'Ninon'),
     ('Nonwoven fabric', 'Nonwoven fabric'), ('Nubuck', 'Nubuck'), ('Nylon', 'Nylon'),
     ('Nytril', 'Nytril'), ('Oilcloth', 'Oilcloth'), ('Olefin', 'Olefin'),
     ('Organdie / Organdy', 'Organdie / Organdy'), ('Organic cotton', 'Organic cotton'),
     ('Organza', 'Organza'), ('Ottoman rib', 'Ottoman rib'), ('Oilcloth', 'Oilcloth'),
     ('Outing Flannel', 'Outing Flannel'), ('Oxford cloth', 'Oxford cloth'),
     ('Paisley', 'Paisley'), ('Panama cloth', 'Panama cloth'), ('Panne', 'Panne'),
     ('Pashmina', 'Pashmina'), ('Patent Leather', 'Patent Leather'),
     ('Peached fabric', 'Peached fabric'), ('Pearlized fabric', 'Pearlized fabric'),
     ('Percale', 'Percale'), ('Performance Knit', 'Performance Knit'),
     ('Permanent press fabric', 'Permanent press fabric'),
     ('Peau de Soie', 'Peau de Soie'), ('Petersham', 'Petersham'),
     ('Pile knit', 'Pile knit'), ('Pile weave', 'Pile weave'), ('Pill', 'Pill'),
     ('Pilot cloth', 'Pilot cloth'), ('Pima cotton', 'Pima cotton'),
     ('Pincord', 'Pincord'), ('Pinpoint', 'Pinpoint'),
     ('Pina Fabric (Pineapple)', 'Pina Fabric (Pineapple)'), ('Pinstripe', 'Pinstripe'),
     ('Pique', 'Pique'), ('Plisse', 'Plisse'), ('Plush', 'Plush'),
     ('Point d’esprit', 'Point d’esprit'), ('Pointelle', 'Pointelle'),
     ('Poiret', 'Poiret'), ('Pongee silk', 'Pongee silk'),
     ('Poodle cloth', 'Poodle cloth'), ('Polo cloth', 'Polo cloth'),
     ('Polished cotton', 'Polished cotton'), ('Polyester', 'Polyester'),
     ('Polyethylene', 'Polyethylene'), ('Polypropylene', 'Polypropylene'),
     ('Polyresin', 'Polyresin'), ('Polystyrene', 'Polystyrene'),
     ('Ponte Roma', 'Ponte Roma'), ('Poplin', 'Poplin'), ('Poult de soi', 'Poult de soi'),
     ('Quilted fabric', 'Quilted fabric'), ('Rabbit hair/wool', 'Rabbit hair/wool'),
     ('Raccoon fur', 'Raccoon fur'), ('Radium', 'Radium'), ('Raffia', 'Raffia'),
     ('Ramie', 'Ramie'), ('Raschel knit', 'Raschel knit'), ('Rayon', 'Rayon'),
     ('Rayon Spandex', 'Rayon Spandex'), ('Repp', 'Repp'), ('Resin', 'Resin'),
     ('Rib Knit', 'Rib Knit'), ('Ribbon', 'Ribbon'), ('Ric Rac', 'Ric Rac'),
     ('Ringspun fabric', 'Ringspun fabric'), ('Ripstop', 'Ripstop'), ('Russet', 'Russet'),
     ('Sailcloth', 'Sailcloth'), ('Santoprene', 'Santoprene'), ('Sarcenet', 'Sarcenet'),
     ('Sarong skirt', 'Sarong skirt'), ('Sateen', 'Sateen'), ('Satin', 'Satin'),
     ('Types of satin and satin weave', 'Types of satin and satin weave'),
     ('Scrim', 'Scrim'), ('Seersucker', 'Seersucker'), ('Serge', 'Serge'),
     ('Serpentine crepe', 'Serpentine crepe'), ('Sequin Fabric', 'Sequin Fabric'),
     ('Sharkskin', 'Sharkskin'), ('Shantung', 'Shantung'), ('Sheeting', 'Sheeting'),
     ('Sherpa (fleece)', 'Sherpa (fleece)'), ('Silesie', 'Silesie'),
     ('Silk Satin', 'Silk Satin'), ('Silk', 'Silk'),
     ('Types of silk fabric and silk weaves', 'Types of silk fabric and silk weaves'),
     ('Simplex', 'Simplex'), ('Sinamay', 'Sinamay'), ('Sisal', 'Sisal'),
     ('Slipper Satin', 'Slipper Satin'), ('Slub jersey', 'Slub jersey'),
     ('Spandex', 'Spandex'), ('Stitch bonded fabric', 'Stitch bonded fabric'),
     ('Stone washed', 'Stone washed'), ('Surah', 'Surah'), ('Suede', 'Suede'),
     ('Suedecloth', 'Suedecloth'), ('Sueded fleece', 'Sueded fleece'),
     ('Supima', 'Supima'), ('Supriva', 'Supriva'), ('Swiss Dot', 'Swiss Dot'),
     ('Synthetic', 'Synthetic'), ('Sweater knit', 'Sweater knit'), ('Tactel', 'Tactel'),
     ('Taffeta', 'Taffeta'), ('Tapa cloth', 'Tapa cloth'), ('Tape yarn', 'Tape yarn'),
     ('Tapestry', 'Tapestry'), ('Tarpaulin', 'Tarpaulin'), ('Tartan', 'Tartan'),
     ('Tattersall', 'Tattersall'), ('Teflon', 'Teflon'), ('Terrycloth', 'Terrycloth'),
     ('Terry Velvet', 'Terry Velvet'), ('Thai silk', 'Thai silk'),
     ('Thermal knit', 'Thermal knit'), ('Ticking', 'Ticking'), ('Tissue', 'Tissue'),
     ('Toweling', 'Toweling'), ('Toile', 'Toile'),
     ('Transparent Velvet', 'Transparent Velvet'), ('Tropical wool', 'Tropical wool'),
     ('Tricot', 'Tricot'), ('Tricotine', 'Tricotine'), ('Tri Acetate', 'Tri Acetate'),
     ('Tricollete', 'Tricollete'), ('Tsumugi Silk', 'Tsumugi Silk'),
     ('Tufted fabric', 'Tufted fabric'), ('Tulle', 'Tulle'),
     ('Tusseh silk / Tussah silk', 'Tusseh silk / Tussah silk'), ('Tweed', 'Tweed'),
     ('Twill', 'Twill'), ('Ultrasuede', 'Ultrasuede'), ('Velboa', 'Velboa'),
     ('Veloutine', 'Veloutine'), ('Velour', 'Velour'), ('Velvet', 'Velvet'),
     ('Velveteen', 'Velveteen'), ('Velveteen plush', 'Velveteen plush'),
     ('Venecia', 'Venecia'), ('Venetian fabric ', 'Venetian fabric '),
     ('Venice', 'Venice'), ('Vichy', 'Vichy'), ('Vicuna', 'Vicuna'), ('Vinyl', 'Vinyl'),
     ('Viscose', 'Viscose'), ('Voile', 'Voile'), ('Washable Paper', 'Washable Paper'),
     ('Wadmal', 'Wadmal'), ('Waffle cloth', 'Waffle cloth'), ('Whipcord', 'Whipcord'),
     ('Wincey', 'Wincey'), ('Wirecloth', 'Wirecloth'), ('Wool', 'Wool'),
     ('Fabrics of wool fabric and weave', 'Fabrics of wool fabric and weave'),
     ('Wool crepe', 'Wool crepe'), ('Woolsy', 'Woolsy'), ('Worsted wool', 'Worsted wool'),
     ('Worsted ', 'Worsted '), ('Worcester', 'Worcester'), ('Yak', 'Yak'),
     ('Yoryu', 'Yoryu'), ('Zanella', 'Zanella'), ('Zephyr', 'Zephyr'),
     ('Zibeline', 'Zibeline')]

CLOTHING_SIZE = [
    ("XS", "X-SMALL"),
    ("X", "SMALL"),
    ("M", "MEDIUM"),
    ("L", "LARGE"),
    ("ALL-SIZE", "ALL-SIZE")
]

ITEM_GENDER = [
    ("F", "FEMALE"),
    ("M", "MALE"),
    ("UNISEX", "UNISEX"),
    ("Kids", "KIDS")
]


def get_image_filename(instance, filename):
    """
    returns the path that contains the address of the post for the image
    """
    post = instance.post
    address = "-".join(item for item in [post.title, post.material_type, post.clothing_type] if item)
    slug = slugify(address)
    return "post_images/%s-%s" % (slug, filename)


class Post(models.Model):
    """
    this code creates a migrations, takes in the class below and creates an sql
    query
    the fields are defined below come teh model defined above
    """
    summary = models.TextField(null=True, blank=True, verbose_name="Describe your product")
    title = models.CharField(max_length=50, verbose_name="Give your ripple a title")
    material_type = models.CharField(max_length=255, verbose_name="material type",
                                     choices=CLOTHING_METRIALS_TYPE_CHOICES)
    clothing_type = models.CharField(max_length=255, verbose_name="Clothing type", choices=CLOTHING_TYPE_CHOICES)
    available_quantity = models.IntegerField(verbose_name="Available quantity", blank=True, null=False)
    quantity_weight = models.IntegerField(verbose_name="Quantity Kilograms")
    item_size = models.CharField(max_length=255, verbose_name="Item size", choices=CLOTHING_SIZE)
    item_gender = models.CharField(max_length=255, verbose_name="Gender", choices=ITEM_GENDER)
    date_posted = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="user_posts", on_delete=models.CASCADE)
    display_q1 = models.CharField(max_length=255, null=False, blank=True, editable=False)
    display_q2 = models.CharField(max_length=255, null=False, blank=True, editable=False)
    display_q3 = models.CharField(max_length=255, null=False, blank=True, editable=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        """
            returns the address of a post
        """
        return self.title

    def get_absolute_url(self):
        """
        this method return a string to redirect the user after posting to that
        post by returning post details the primary key of the newly created
        post

        the pk is used to identify each post, meaning when each post is created,
        it's assigned a pk number
        :return:
        """
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        """
        overwriting the django save method
        by passing in the estimated price into the price before it is saved
        """
        display_q1 = self.material_type if 46 > len(self.material_type) else (self.material_type[:45]) + ".."
        display_q2 = self.clothing_type if self.material_type is not None or 46 > len(self.clothing_type) \
            else (self.clothing_type[:45]) + ".."
        title = self.title.upper()
        self.title = title
        self.display_q1 = display_q1
        self.display_q2 = display_q2
        super().save(force_insert, force_update, *args, **kwargs)


class PostImage(models.Model):
    """
    the model is used for image posting and image deletion
    """
    image = models.ImageField('images', upload_to=get_image_filename, null=True, blank=True)
    post = models.ForeignKey(Post, related_name='post_images', on_delete=models.CASCADE)

    def delete(self):
        """delete the file when the object is deleted"""
        self.image.delete()
        super(PostImage, self).delete()


# TODO create review model

"""
app from the solution 
requirement 
sustainable to be a key
supporting small business and the local community


brand image for people buying from the local store
"""
