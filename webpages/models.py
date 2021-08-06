from authentication.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.db import models

CLOTHING_TYPE_CHOICES = \
    [('Androgynous fashion style', 'Androgynous fashion style'), ('Ankara Fashion Style', 'Ankara Fashion Style'),
     ('Arthoe Fashion Style', 'Arthoe Fashion Style'), ('Artsy Fashion style', 'Artsy Fashion style'),
     ('Biker fashion', 'Biker fashion'), ('Boho/Bohemian chic', 'Boho/Bohemian chic'),
     ('Business Casual', 'Business Casual'), ('Camp Style', 'Camp Style'), ('Casual Chic Style', 'Casual Chic Style'),
     ('Chave culture Style', 'Chave culture Style'), ('Cosplay Fashion', 'Cosplay Fashion'),
     ('Cowgirl fashion style', 'Cowgirl fashion style'), ('E girl', 'E girl'),
     ('Ethnic fashion style ', 'Ethnic fashion style '), ('Evening Black Tie', 'Evening Black Tie'),
     ('Flamboyant style', 'Flamboyant style'), ('Flapper fashion (20s look),', 'Flapper fashion (20s look),'),
     ('Formal Office Wear', 'Formal Office Wear'), ('Garconne look', 'Garconne look'),
     ('Geeky chic Style', 'Geeky chic Style'), ('Girl next door fashion style', 'Girl next door fashion style'),
     ('Girly Style ', 'Girly Style '), ('Goth Fashion', 'Goth Fashion'), ('Gothic lolita style', 'Gothic lolita style'),
     ('Grunge style', 'Grunge style'), ('Haute Couture', 'Haute Couture'), ('Hip Hop Style', 'Hip Hop Style'),
     ('Kawaii fashion', 'Kawaii fashion'), ('Lagenlook Fashion style', 'Lagenlook Fashion style'),
     ('Lolita Fashion', 'Lolita Fashion'), ('Maternity Style', 'Maternity Style'), ('Military style', 'Military style'),
     ('Modest fashion', 'Modest fashion'), ('Prairie chic style', 'Prairie chic style'),
     ('Preppy style', 'Preppy style'),
     ('Psychedelic Fashion style', 'Psychedelic Fashion style'), ('Punk', 'Punk'), ('Rave fashion', 'Rave fashion'),
     ('Retro Fashion', 'Retro Fashion'), ('Rocker Chic Style', 'Rocker Chic Style'),
     ('Scene fashion style', 'Scene fashion style'), ('Skateboarders', 'Skateboarders'), ('Sports Wear', 'Sports Wear'),
     ('Streetwear Style', 'Streetwear Style'), ('Tomboy', 'Tomboy'),
     ('Vacation (Resort), style', 'Vacation (Resort), style')]

CLOTHING_METRIALS_TYPE_CHOICES = \
    [(' Ardass', ' Ardass'), (' Ardass', ' Ardass'), ('Aba', 'Aba'), ('Aba', 'Aba'), ('Abaca', 'Abaca'),
     ('Abaca', 'Abaca'), ('Acetate ', 'Acetate '), ('Acetate ', 'Acetate '), ('Acrylic fabric', 'Acrylic fabric'),
     ('Acrylic fabric', 'Acrylic fabric'), ('Active Comfort Denim', 'Active Comfort Denim'),
     ('Active Comfort Denim', 'Active Comfort Denim'), ('Admiralty cloth', 'Admiralty cloth'),
     ('Admiralty cloth', 'Admiralty cloth'), ('Aerophane', 'Aerophane'), ('Aerophane', 'Aerophane'),
     ('Aertex', 'Aertex'), ('Aertex', 'Aertex'), ('Aida Canvas / Aida cloth', 'Aida Canvas / Aida cloth'),
     ('Aida Canvas / Aida cloth', 'Aida Canvas / Aida cloth'), ('Airplane cloth', 'Airplane cloth'),
     ('Airplane cloth', 'Airplane cloth'), ('Albatross', 'Albatross'), ('Albatross', 'Albatross'),
     ('Albert Cloth', 'Albert Cloth'), ('Albert Cloth', 'Albert Cloth'), ('Alepine', 'Alepine'), ('Alepine', 'Alepine'),
     ('Alpaca', 'Alpaca'), ('Alpaca', 'Alpaca'), ('Alpaca crepe', 'Alpaca crepe'), ('Alpaca crepe', 'Alpaca crepe'),
     ('American Pima Cotton', 'American Pima Cotton'), ('American Pima Cotton', 'American Pima Cotton'),
     ('Angola', 'Angola'), ('Angola', 'Angola'), ('Angora fibres', 'Angora fibres'), ('Angora fibres', 'Angora fibres'),
     ('Anti-pill', 'Anti-pill'), ('Anti-pill', 'Anti-pill'), ('Antique satin', 'Antique satin'),
     ('Antique satin', 'Antique satin'), ('Argyle', 'Argyle'), ('Argyle', 'Argyle'), ('Armure', 'Armure'),
     ('Armure', 'Armure'), ('Art Linen', 'Art Linen'), ('Art Linen', 'Art Linen'), ('Astrakhan', 'Astrakhan'),
     ('Astrakhan', 'Astrakhan'), ('Atlas', 'Atlas'), ('Atlas', 'Atlas'), ('Awnings', 'Awnings'), ('Awnings', 'Awnings'),
     ('Baby Combing Wool', 'Baby Combing Wool'), ('Baby Combing Wool', 'Baby Combing Wool'), ('Baft', 'Baft'),
     ('Baft', 'Baft'), ('Bagheera Velvet', 'Bagheera Velvet'), ('Bagheera Velvet', 'Bagheera Velvet'),
     ('Baize', 'Baize'), ('Baize', 'Baize'), ('Ballistic', 'Ballistic'), ('Ballistic', 'Ballistic'),
     ('Balloon cloth', 'Balloon cloth'), ('Balloon cloth', 'Balloon cloth'), ('Bamboo fibers', 'Bamboo fibers'),
     ('Bamboo fibers', 'Bamboo fibers'), ('Banana Fabric', 'Banana Fabric'), ('Banana Fabric', 'Banana Fabric'),
     ('Banbury plush', 'Banbury plush'), ('Banbury plush', 'Banbury plush'), ('Bandana', 'Bandana'),
     ('Bandana', 'Bandana'), ('Bark Cloth', 'Bark Cloth'), ('Bark Cloth', 'Bark Cloth'),
     ('Baronet satin', 'Baronet satin'), ('Baronet satin', 'Baronet satin'), ('Basket weave', 'Basket weave'),
     ('Basket weave', 'Basket weave'), ('Bathroom Blanketing (Blanket cloth)', 'Bathroom Blanketing (Blanket cloth)'),
     ('Bathroom Blanketing (Blanket cloth)', 'Bathroom Blanketing (Blanket cloth)'), ('Batik', 'Batik'),
     ('Batik', 'Batik'), ('Batiste', 'Batiste'), ('Batiste', 'Batiste'), ('Batt or Batting', 'Batt or Batting'),
     ('Batt or Batting', 'Batt or Batting'), ('Beaded', 'Beaded'), ('Beaded', 'Beaded'),
     ('Beaver cloth', 'Beaver cloth'), ('Beaver cloth', 'Beaver cloth'), ('Bedford (Cord)', 'Bedford (Cord)'),
     ('Bedford (Cord)', 'Bedford (Cord)'), ('Belly Wool', 'Belly Wool'), ('Belly Wool', 'Belly Wool'),
     ('Bemberg', 'Bemberg'), ('Bemberg', 'Bemberg'), ('Bengaline /Faille', 'Bengaline /Faille'),
     ('Bengaline /Faille', 'Bengaline /Faille'), ('Berber fleece', 'Berber fleece'), ('Berber fleece', 'Berber fleece'),
     ('Bicast leather (PU leather)', 'Bicast leather (PU leather)'),
     ('Bicast leather (PU leather)', 'Bicast leather (PU leather)'), ('Binding cloth', 'Binding cloth'),
     ('Binding cloth', 'Binding cloth'), ('Biopolished cotton', 'Biopolished cotton'),
     ('Biopolished cotton', 'Biopolished cotton'), ('Black Wool', 'Black Wool'), ('Black Wool', 'Black Wool'),
     ('Blanket cloth', 'Blanket cloth'), ('Blanket cloth', 'Blanket cloth'), ('Blends', 'Blends'), ('Blends', 'Blends'),
     ('Bobbinet', 'Bobbinet'), ('Bobbinet', 'Bobbinet'), ('Boiled Wool', 'Boiled Wool'), ('Boiled Wool', 'Boiled Wool'),
     ('Bombazine', 'Bombazine'), ('Bombazine', 'Bombazine'), ('Bombazine', 'Bombazine'), ('Bombazine', 'Bombazine'),
     ('Bonded leather', 'Bonded leather'), ('Bonded leather', 'Bonded leather'), ('Botany Wools', 'Botany Wools'),
     ('Botany Wools', 'Botany Wools'), ('Boynge', 'Boynge'), ('Boynge', 'Boynge'),
     ('Breech or Britch Wool', 'Breech or Britch Wool'), ('Breech or Britch Wool', 'Breech or Britch Wool'),
     ('Brocade', 'Brocade'), ('Brocade', 'Brocade'), ('Brocatelle', 'Brocatelle'), ('Brocatelle', 'Brocatelle'),
     ('Broderie Anglaise', 'Broderie Anglaise'), ('Broderie Anglaise', 'Broderie Anglaise'),
     ('Brushed Wool', 'Brushed Wool'), ('Brushed Wool', 'Brushed Wool'), ('Buck Fleece', 'Buck Fleece'),
     ('Buck Fleece', 'Buck Fleece'), ('Bunting', 'Bunting'), ('Bunting', 'Bunting'), ('Burlap', 'Burlap'),
     ('Burlap', 'Burlap'), ('Burlap', 'Burlap'), ('Burlap', 'Burlap'), ('Calico', 'Calico'), ('Calico', 'Calico'),
     ('Cambric', 'Cambric'), ('Cambric', 'Cambric'), ('Camel’s Hair', 'Camel’s Hair'), ('Camel’s Hair', 'Camel’s Hair'),
     ('Camlet', 'Camlet'), ('Camlet', 'Camlet'), ('Canton crepe', 'Canton crepe'), ('Canton crepe', 'Canton crepe'),
     ('Canvas', 'Canvas'), ('Canvas', 'Canvas'), ('Carpet Wool', 'Carpet Wool'), ('Carpet Wool', 'Carpet Wool'),
     ('Casement', 'Casement'), ('Casement', 'Casement'), ('Cashgora', 'Cashgora'), ('Cashgora', 'Cashgora'),
     ('Cashmere', 'Cashmere'), ('Cashmere', 'Cashmere'), ('Cashmerlon', 'Cashmerlon'), ('Cashmerlon', 'Cashmerlon'),
     ('Cavalry Twill', 'Cavalry Twill'), ('Cavalry Twill', 'Cavalry Twill'),
     ('Cerecloth / altar cloth', 'Cerecloth / altar cloth'), ('Cerecloth / altar cloth', 'Cerecloth / altar cloth'),
     ('Challis', 'Challis'), ('Challis', 'Challis'), ('Chambray / Chambric', 'Chambray / Chambric'),
     ('Chambray / Chambric', 'Chambray / Chambric'), ('Chamoise', 'Chamoise'), ('Chamoise', 'Chamoise'),
     ('Chanel tweed', 'Chanel tweed'), ('Chanel tweed', 'Chanel tweed'), ('Chantilly lace', 'Chantilly lace'),
     ('Chantilly lace', 'Chantilly lace'), ('Charmeuse', 'Charmeuse'), ('Charmeuse', 'Charmeuse'),
     ('Charvet silk', 'Charvet silk'), ('Charvet silk', 'Charvet silk'), ('Checks', 'Checks'), ('Checks', 'Checks'),
     ('Cheese cloth', 'Cheese cloth'), ('Cheese cloth', 'Cheese cloth'), ('Chenille', 'Chenille'),
     ('Chenille', 'Chenille'), ('Cheviot', 'Cheviot'), ('Cheviot', 'Cheviot'), ('Chevron', 'Chevron'),
     ('Chevron', 'Chevron'), ('Chiffon', 'Chiffon'), ('Chiffon', 'Chiffon'), ('China silk ', 'China silk '),
     ('China silk ', 'China silk '), ('Chinchilla cloth', 'Chinchilla cloth'), ('Chinchilla cloth', 'Chinchilla cloth'),
     ('Chino', 'Chino'), ('Chino', 'Chino'), ('Chint', 'Chint'), ('Chint', 'Chint'), ('Chintz', 'Chintz'),
     ('Chintz', 'Chintz'), ('Chire', 'Chire'), ('Chire', 'Chire'), ('Chite', 'Chite'), ('Chite', 'Chite'),
     ('Cisele velvet', 'Cisele velvet'), ('Cisele velvet', 'Cisele velvet'), ('Cloque', 'Cloque'), ('Cloque', 'Cloque'),
     ('Coating', 'Coating'), ('Coating', 'Coating'), ('Colorfast', 'Colorfast'), ('Colorfast', 'Colorfast'),
     ('Combed cotton', 'Combed cotton'), ('Combed cotton', 'Combed cotton'), ('Corduroy', 'Corduroy'),
     ('Corduroy', 'Corduroy'), ('Cottagora', 'Cottagora'), ('Cottagora', 'Cottagora'), ('Cotton', 'Cotton'),
     ('Cotton', 'Cotton'), ('Cotton Lawn', 'Cotton Lawn'), ('Cotton Lawn', 'Cotton Lawn'),
     ('Cotton backed Satin', 'Cotton backed Satin'), ('Cotton backed Satin', 'Cotton backed Satin'),
     ('Cotton voile', 'Cotton voile'), ('Cotton voile', 'Cotton voile'), ('Crazy Horse', 'Crazy Horse'),
     ('Crazy Horse', 'Crazy Horse'), ('Crepe', 'Crepe'), ('Crepe', 'Crepe'), ('Crepe back satin', 'Crepe back satin'),
     ('Crepe back satin', 'Crepe back satin'), ('Crepe de chine', 'Crepe de chine'),
     ('Crepe de chine', 'Crepe de chine'), ('Cretonne', 'Cretonne'), ('Cretonne', 'Cretonne'),
     ('Crinkle satin', 'Crinkle satin'), ('Crinkle satin', 'Crinkle satin'), ('Crinoline ', 'Crinoline '),
     ('Crinoline ', 'Crinoline '), ('Crinoline net', 'Crinoline net'), ('Crinoline net', 'Crinoline net'),
     ('Crochet', 'Crochet'), ('Crochet', 'Crochet'), ('Cupro', 'Cupro'), ('Cupro', 'Cupro'), ('Dacron', 'Dacron'),
     ('Dacron', 'Dacron'), ('Damask', 'Damask'), ('Damask', 'Damask'), ('Dazzle', 'Dazzle'), ('Dazzle', 'Dazzle'),
     ('Deerskin', 'Deerskin'), ('Deerskin', 'Deerskin'), ('Denim / dungaree / jean', 'Denim / dungaree / jean'),
     ('Denim / dungaree / jean', 'Denim / dungaree / jean'), ('Diaper cloth', 'Diaper cloth'),
     ('Diaper cloth', 'Diaper cloth'), ('Different linen fabric', 'Different linen fabric'),
     ('Different linen fabric', 'Different linen fabric'), ('Dimity', 'Dimity'), ('Dimity', 'Dimity'),
     ('Doeskin', 'Doeskin'), ('Doeskin', 'Doeskin'), ('Dommet flannel', 'Dommet flannel'),
     ('Dommet flannel', 'Dommet flannel'), ('Donegal', 'Donegal'), ('Donegal', 'Donegal'), ('Dorian', 'Dorian'),
     ('Dorian', 'Dorian'), ('Dotted Swiss', 'Dotted Swiss'), ('Dotted Swiss', 'Dotted Swiss'),
     ('Double Gauze', 'Double Gauze'), ('Double Gauze', 'Double Gauze'), ('Double cloth', 'Double cloth'),
     ('Double cloth', 'Double cloth'), ('Double knit', 'Double knit'), ('Double knit', 'Double knit'), ('Down', 'Down'),
     ('Down', 'Down'), ('Dress net', 'Dress net'), ('Dress net', 'Dress net'), ('Drill', 'Drill'), ('Drill', 'Drill'),
     ('Duchess satin', 'Duchess satin'), ('Duchess satin', 'Duchess satin'), ('Duck cloth', 'Duck cloth'),
     ('Duck cloth', 'Duck cloth'), ('Duffel', 'Duffel'), ('Duffel', 'Duffel'), ('Dupioni', 'Dupioni'),
     ('Dupioni', 'Dupioni'), ('Duplex prints', 'Duplex prints'), ('Duplex prints', 'Duplex prints'),
     ('Duvetyne', 'Duvetyne'), ('Duvetyne', 'Duvetyne'), ('Egyptian cotton', 'Egyptian cotton'),
     ('Egyptian cotton', 'Egyptian cotton'), ('Elastane', 'Elastane'), ('Elastane', 'Elastane'),
     ('Elastique', 'Elastique'), ('Elastique', 'Elastique'), ('Embroidered fabric', 'Embroidered fabric'),
     ('Embroidered fabric', 'Embroidered fabric'), ('English net', 'English net'), ('English net', 'English net'),
     ('Eolienne', 'Eolienne'), ('Eolienne', 'Eolienne'), ('Epyngle', 'Epyngle'), ('Epyngle', 'Epyngle'),
     ('Eyelash', 'Eyelash'), ('Eyelash', 'Eyelash'), ('Eyelet', 'Eyelet'), ('Eyelet', 'Eyelet'),
     ('Fabrics of wool fabric and weave', 'Fabrics of wool fabric and weave'),
     ('Fabrics of wool fabric and weave', 'Fabrics of wool fabric and weave'), ('Faconne', 'Faconne'),
     ('Faconne', 'Faconne'), ('Faille', 'Faille'), ('Faille', 'Faille'), ('Fake fur', 'Fake fur'),
     ('Fake fur', 'Fake fur'), ('Faux Fur', 'Faux Fur'), ('Faux Fur', 'Faux Fur'), ('Faux leather', 'Faux leather'),
     ('Faux leather', 'Faux leather'), ('Faux silk', 'Faux silk'), ('Faux silk', 'Faux silk'), ('Feathers', 'Feathers'),
     ('Feathers', 'Feathers'), ('Felt', 'Felt'), ('Felt', 'Felt'), ('Flanellette', 'Flanellette'),
     ('Flanellette', 'Flanellette'), ('Flannel', 'Flannel'), ('Flannel', 'Flannel'), ('Flax', 'Flax'), ('Flax', 'Flax'),
     ('Foulard', 'Foulard'), ('Foulard', 'Foulard'), ('French terry', 'French terry'), ('French terry', 'French terry'),
     ('Frieze', 'Frieze'), ('Frieze', 'Frieze'), ('Frieze', 'Frieze'), ('Frieze', 'Frieze'),
     ('Full-grain leather', 'Full-grain leather'), ('Full-grain leather', 'Full-grain leather'), ('Fur', 'Fur'),
     ('Fur', 'Fur'), ('Fustian', 'Fustian'), ('Fustian', 'Fustian'), ('Gabardine', 'Gabardine'),
     ('Gabardine', 'Gabardine'), ('Gauze', 'Gauze'), ('Gauze', 'Gauze'), ('Georgette', 'Georgette'),
     ('Georgette', 'Georgette'), ('Gingham', 'Gingham'), ('Gingham', 'Gingham'), ('Glen checks', 'Glen checks'),
     ('Glen checks', 'Glen checks'), ('Gossamer', 'Gossamer'), ('Gossamer', 'Gossamer'), ('Grosgrain', 'Grosgrain'),
     ('Grosgrain', 'Grosgrain'), ('Habutai', 'Habutai'), ('Habutai', 'Habutai'), ('Haircloth', 'Haircloth'),
     ('Haircloth', 'Haircloth'), ('Handkerchief Linen', 'Handkerchief Linen'),
     ('Handkerchief Linen', 'Handkerchief Linen'), ('Hemp', 'Hemp'), ('Hemp', 'Hemp'), ('Hessian', 'Hessian'),
     ('Hessian', 'Hessian'), ('Homespun', 'Homespun'), ('Homespun', 'Homespun'), ('Hopsacking', 'Hopsacking'),
     ('Hopsacking', 'Hopsacking'), ('Huckaback', 'Huckaback'), ('Huckaback', 'Huckaback'), ('Ikat', 'Ikat'),
     ('Ikat', 'Ikat'), ('Illusion', 'Illusion'), ('Illusion', 'Illusion'), ('Interlock', 'Interlock'),
     ('Interlock', 'Interlock'), ('Irish poplin', 'Irish poplin'), ('Irish poplin', 'Irish poplin'),
     ('Jaconet', 'Jaconet'), ('Jaconet', 'Jaconet'), ('Jacquard', 'Jacquard'), ('Jacquard', 'Jacquard'),
     ('Jersey', 'Jersey'), ('Jersey', 'Jersey'), ('Jute', 'Jute'), ('Jute', 'Jute'), ('Khakhi', 'Khakhi'),
     ('Khakhi', 'Khakhi'), ('Kidskin', 'Kidskin'), ('Kidskin', 'Kidskin'), ('Knit', 'Knit'), ('Knit', 'Knit'),
     ('Knitted fabric ', 'Knitted fabric '), ('Knitted fabric ', 'Knitted fabric '), ('Lace', 'Lace'), ('Lace', 'Lace'),
     ('Lambskin', 'Lambskin'), ('Lambskin', 'Lambskin'), ('Lamb’s wool', 'Lamb’s wool'), ('Lamb’s wool', 'Lamb’s wool'),
     ('Layette', 'Layette'), ('Layette', 'Layette'), ('Leather', 'Leather'), ('Leather', 'Leather'),
     ('Leathertte', 'Leathertte'), ('Leathertte', 'Leathertte'), ('Linen', 'Linen'), ('Linen', 'Linen'),
     ('Linsey woolsey', 'Linsey woolsey'), ('Linsey woolsey', 'Linsey woolsey'), ('Lint', 'Lint'), ('Lint', 'Lint'),
     ('Liquid cotton', 'Liquid cotton'), ('Liquid cotton', 'Liquid cotton'), ('Lisle', 'Lisle'), ('Lisle', 'Lisle'),
     ('Llama', 'Llama'), ('Llama', 'Llama'), ('Loden Fabric', 'Loden Fabric'), ('Loden Fabric', 'Loden Fabric'),
     ('Lurex', 'Lurex'), ('Lurex', 'Lurex'), ('Lycra', 'Lycra'), ('Lycra', 'Lycra'), ('Lycra', 'Lycra'),
     ('Lycra', 'Lycra'), ('Macinaw', 'Macinaw'), ('Macinaw', 'Macinaw'), ('Mackinosh', 'Mackinosh'),
     ('Mackinosh', 'Mackinosh'), ('Macrame', 'Macrame'), ('Macrame', 'Macrame'), ('Madras', 'Madras'),
     ('Madras', 'Madras'), ('Marceline', 'Marceline'), ('Marceline', 'Marceline'), ('Marled', 'Marled'),
     ('Marled', 'Marled'), ('Marquissette', 'Marquissette'), ('Marquissette', 'Marquissette'), ('Marvello', 'Marvello'),
     ('Marvello', 'Marvello'), ('Matelasse', 'Matelasse'), ('Matelasse', 'Matelasse'), ('Matte fabric', 'Matte fabric'),
     ('Matte fabric', 'Matte fabric'), ('Melange', 'Melange'), ('Melange', 'Melange'), ('Melton', 'Melton'),
     ('Melton', 'Melton'), ('Merino  wool', 'Merino  wool'), ('Merino  wool', 'Merino  wool'), ('Mesh', 'Mesh'),
     ('Mesh', 'Mesh'), ('Messaline', 'Messaline'), ('Messaline', 'Messaline'), ('Microfiber', 'Microfiber'),
     ('Microfiber', 'Microfiber'), ('Milanese', 'Milanese'), ('Milanese', 'Milanese'), ('Milk yarn', 'Milk yarn'),
     ('Milk yarn', 'Milk yarn'), ('Modal', 'Modal'), ('Modal', 'Modal'), ('Mohair', 'Mohair'), ('Mohair', 'Mohair'),
     ('Moire', 'Moire'), ('Moire', 'Moire'), ('Moleskin', 'Moleskin'), ('Moleskin', 'Moleskin'),
     ('Monks cloth', 'Monks cloth'), ('Monks cloth', 'Monks cloth'), ('Moss crepe', 'Moss crepe'),
     ('Moss crepe', 'Moss crepe'), ('Mother of pearl', 'Mother of pearl'), ('Mother of pearl', 'Mother of pearl'),
     ('Mull', 'Mull'), ('Mull', 'Mull'), ('Muslin', 'Muslin'), ('Muslin', 'Muslin'), ('Nankeen', 'Nankeen'),
     ('Nankeen', 'Nankeen'), ('Nappa Leather', 'Nappa Leather'), ('Nappa Leather', 'Nappa Leather'),
     ('Neoprene', 'Neoprene'), ('Neoprene', 'Neoprene'), ('Nep', 'Nep'), ('Nep', 'Nep'), ('Net fabric', 'Net fabric'),
     ('Net fabric', 'Net fabric'), ('Netting', 'Netting'), ('Netting', 'Netting'), ('Ninon', 'Ninon'),
     ('Ninon', 'Ninon'), ('Nonwoven fabric', 'Nonwoven fabric'), ('Nonwoven fabric', 'Nonwoven fabric'),
     ('Nubuck', 'Nubuck'), ('Nubuck', 'Nubuck'), ('Nylon', 'Nylon'), ('Nylon', 'Nylon'), ('Nytril', 'Nytril'),
     ('Nytril', 'Nytril'), ('Oilcloth', 'Oilcloth'), ('Oilcloth', 'Oilcloth'), ('Oilcloth', 'Oilcloth'),
     ('Oilcloth', 'Oilcloth'), ('Olefin', 'Olefin'), ('Olefin', 'Olefin'), ('Organdie / Organdy', 'Organdie / Organdy'),
     ('Organdie / Organdy', 'Organdie / Organdy'), ('Organic cotton', 'Organic cotton'),
     ('Organic cotton', 'Organic cotton'), ('Organza', 'Organza'), ('Organza', 'Organza'),
     ('Ottoman rib', 'Ottoman rib'), ('Ottoman rib', 'Ottoman rib'), ('Outing Flannel', 'Outing Flannel'),
     ('Outing Flannel', 'Outing Flannel'), ('Oxford cloth', 'Oxford cloth'), ('Oxford cloth', 'Oxford cloth'),
     ('Paisley', 'Paisley'), ('Paisley', 'Paisley'), ('Panama cloth', 'Panama cloth'), ('Panama cloth', 'Panama cloth'),
     ('Panne', 'Panne'), ('Panne', 'Panne'), ('Pashmina', 'Pashmina'), ('Pashmina', 'Pashmina'),
     ('Patent Leather', 'Patent Leather'), ('Patent Leather', 'Patent Leather'), ('Peached fabric', 'Peached fabric'),
     ('Peached fabric', 'Peached fabric'), ('Pearlized fabric', 'Pearlized fabric'),
     ('Pearlized fabric', 'Pearlized fabric'), ('Peau de Soie', 'Peau de Soie'), ('Peau de Soie', 'Peau de Soie'),
     ('Percale', 'Percale'), ('Percale', 'Percale'), ('Performance Knit', 'Performance Knit'),
     ('Performance Knit', 'Performance Knit'), ('Permanent press fabric', 'Permanent press fabric'),
     ('Permanent press fabric', 'Permanent press fabric'), ('Petersham', 'Petersham'), ('Petersham', 'Petersham'),
     ('Pile knit', 'Pile knit'), ('Pile knit', 'Pile knit'), ('Pile weave', 'Pile weave'), ('Pile weave', 'Pile weave'),
     ('Pill', 'Pill'), ('Pill', 'Pill'), ('Pilot cloth', 'Pilot cloth'), ('Pilot cloth', 'Pilot cloth'),
     ('Pima cotton', 'Pima cotton'), ('Pima cotton', 'Pima cotton'),
     ('Pina Fabric (Pineapple)', 'Pina Fabric (Pineapple)'), ('Pina Fabric (Pineapple)', 'Pina Fabric (Pineapple)'),
     ('Pincord', 'Pincord'), ('Pincord', 'Pincord'), ('Pinpoint', 'Pinpoint'), ('Pinpoint', 'Pinpoint'),
     ('Pinstripe', 'Pinstripe'), ('Pinstripe', 'Pinstripe'), ('Pique', 'Pique'), ('Pique', 'Pique'),
     ('Plisse', 'Plisse'), ('Plisse', 'Plisse'), ('Plush', 'Plush'), ('Plush', 'Plush'),
     ('Point d’esprit', 'Point d’esprit'), ('Point d’esprit', 'Point d’esprit'), ('Pointelle', 'Pointelle'),
     ('Pointelle', 'Pointelle'), ('Poiret', 'Poiret'), ('Poiret', 'Poiret'), ('Polished cotton', 'Polished cotton'),
     ('Polished cotton', 'Polished cotton'), ('Polo cloth', 'Polo cloth'), ('Polo cloth', 'Polo cloth'),
     ('Polyester', 'Polyester'), ('Polyester', 'Polyester'), ('Polyethylene', 'Polyethylene'),
     ('Polyethylene', 'Polyethylene'), ('Polypropylene', 'Polypropylene'), ('Polypropylene', 'Polypropylene'),
     ('Polyresin', 'Polyresin'), ('Polyresin', 'Polyresin'), ('Polystyrene', 'Polystyrene'),
     ('Polystyrene', 'Polystyrene'), ('Pongee silk', 'Pongee silk'), ('Pongee silk', 'Pongee silk'),
     ('Ponte Roma', 'Ponte Roma'), ('Ponte Roma', 'Ponte Roma'), ('Poodle cloth', 'Poodle cloth'),
     ('Poodle cloth', 'Poodle cloth'), ('Poplin', 'Poplin'), ('Poplin', 'Poplin'), ('Poult de soi', 'Poult de soi'),
     ('Poult de soi', 'Poult de soi'), ('Quilted fabric', 'Quilted fabric'), ('Quilted fabric', 'Quilted fabric'),
     ('Rabbit hair/wool', 'Rabbit hair/wool'), ('Rabbit hair/wool', 'Rabbit hair/wool'), ('Raccoon fur', 'Raccoon fur'),
     ('Raccoon fur', 'Raccoon fur'), ('Radium', 'Radium'), ('Radium', 'Radium'), ('Raffia', 'Raffia'),
     ('Raffia', 'Raffia'), ('Ramie', 'Ramie'), ('Ramie', 'Ramie'), ('Raschel knit', 'Raschel knit'),
     ('Raschel knit', 'Raschel knit'), ('Rayon', 'Rayon'), ('Rayon', 'Rayon'), ('Rayon Spandex', 'Rayon Spandex'),
     ('Rayon Spandex', 'Rayon Spandex'), ('Repp', 'Repp'), ('Repp', 'Repp'), ('Resin', 'Resin'), ('Resin', 'Resin'),
     ('Rib Knit', 'Rib Knit'), ('Rib Knit', 'Rib Knit'), ('Ribbon', 'Ribbon'), ('Ribbon', 'Ribbon'),
     ('Ric Rac', 'Ric Rac'), ('Ric Rac', 'Ric Rac'), ('Ringspun fabric', 'Ringspun fabric'),
     ('Ringspun fabric', 'Ringspun fabric'), ('Ripstop', 'Ripstop'), ('Ripstop', 'Ripstop'), ('Russet', 'Russet'),
     ('Russet', 'Russet'), ('Sailcloth', 'Sailcloth'), ('Sailcloth', 'Sailcloth'), ('Santoprene', 'Santoprene'),
     ('Santoprene', 'Santoprene'), ('Sarcenet', 'Sarcenet'), ('Sarcenet', 'Sarcenet'), ('Sarong skirt', 'Sarong skirt'),
     ('Sarong skirt', 'Sarong skirt'), ('Sateen', 'Sateen'), ('Sateen', 'Sateen'), ('Satin', 'Satin'),
     ('Satin', 'Satin'), ('Scrim', 'Scrim'), ('Scrim', 'Scrim'), ('Seersucker', 'Seersucker'),
     ('Seersucker', 'Seersucker'), ('Sequin Fabric', 'Sequin Fabric'), ('Sequin Fabric', 'Sequin Fabric'),
     ('Serge', 'Serge'), ('Serge', 'Serge'), ('Serpentine crepe', 'Serpentine crepe'),
     ('Serpentine crepe', 'Serpentine crepe'), ('Shantung', 'Shantung'), ('Shantung', 'Shantung'),
     ('Sharkskin', 'Sharkskin'), ('Sharkskin', 'Sharkskin'), ('Sheeting', 'Sheeting'), ('Sheeting', 'Sheeting'),
     ('Sherpa (fleece)', 'Sherpa (fleece)'), ('Sherpa (fleece)', 'Sherpa (fleece)'), ('Silesie', 'Silesie'),
     ('Silesie', 'Silesie'), ('Silk', 'Silk'), ('Silk', 'Silk'), ('Silk Satin', 'Silk Satin'),
     ('Silk Satin', 'Silk Satin'), ('Simplex', 'Simplex'), ('Simplex', 'Simplex'), ('Sinamay', 'Sinamay'),
     ('Sinamay', 'Sinamay'), ('Sisal', 'Sisal'), ('Sisal', 'Sisal'), ('Slipper Satin', 'Slipper Satin'),
     ('Slipper Satin', 'Slipper Satin'), ('Slub jersey', 'Slub jersey'), ('Slub jersey', 'Slub jersey'),
     ('Spandex', 'Spandex'), ('Spandex', 'Spandex'), ('Stitch bonded fabric', 'Stitch bonded fabric'),
     ('Stitch bonded fabric', 'Stitch bonded fabric'), ('Stone washed', 'Stone washed'),
     ('Stone washed', 'Stone washed'), ('Suede', 'Suede'), ('Suede', 'Suede'), ('Suedecloth', 'Suedecloth'),
     ('Suedecloth', 'Suedecloth'), ('Sueded fleece', 'Sueded fleece'), ('Sueded fleece', 'Sueded fleece'),
     ('Supima', 'Supima'), ('Supima', 'Supima'), ('Supriva', 'Supriva'), ('Supriva', 'Supriva'), ('Surah', 'Surah'),
     ('Surah', 'Surah'), ('Sweater knit', 'Sweater knit'), ('Sweater knit', 'Sweater knit'), ('Swiss Dot', 'Swiss Dot'),
     ('Swiss Dot', 'Swiss Dot'), ('Synthetic', 'Synthetic'), ('Synthetic', 'Synthetic'), ('Tactel', 'Tactel'),
     ('Tactel', 'Tactel'), ('Taffeta', 'Taffeta'), ('Taffeta', 'Taffeta'), ('Tapa cloth', 'Tapa cloth'),
     ('Tapa cloth', 'Tapa cloth'), ('Tape yarn', 'Tape yarn'), ('Tape yarn', 'Tape yarn'), ('Tapestry', 'Tapestry'),
     ('Tapestry', 'Tapestry'), ('Tarpaulin', 'Tarpaulin'), ('Tarpaulin', 'Tarpaulin'), ('Tartan', 'Tartan'),
     ('Tartan', 'Tartan'), ('Tattersall', 'Tattersall'), ('Tattersall', 'Tattersall'), ('Teflon', 'Teflon'),
     ('Teflon', 'Teflon'), ('Terry Velvet', 'Terry Velvet'), ('Terry Velvet', 'Terry Velvet'),
     ('Terrycloth', 'Terrycloth'), ('Terrycloth', 'Terrycloth'), ('Thai silk', 'Thai silk'), ('Thai silk', 'Thai silk'),
     ('Thermal knit', 'Thermal knit'), ('Thermal knit', 'Thermal knit'), ('Ticking', 'Ticking'), ('Ticking', 'Ticking'),
     ('Tissue', 'Tissue'), ('Tissue', 'Tissue'), ('Toile', 'Toile'), ('Toile', 'Toile'), ('Toweling', 'Toweling'),
     ('Toweling', 'Toweling'), ('Transparent Velvet', 'Transparent Velvet'),
     ('Transparent Velvet', 'Transparent Velvet'), ('Tri Acetate', 'Tri Acetate'), ('Tri Acetate', 'Tri Acetate'),
     ('Tricollete', 'Tricollete'), ('Tricollete', 'Tricollete'), ('Tricot', 'Tricot'), ('Tricot', 'Tricot'),
     ('Tricotine', 'Tricotine'), ('Tricotine', 'Tricotine'), ('Tropical wool', 'Tropical wool'),
     ('Tropical wool', 'Tropical wool'), ('Tsumugi Silk', 'Tsumugi Silk'), ('Tsumugi Silk', 'Tsumugi Silk'),
     ('Tufted fabric', 'Tufted fabric'), ('Tufted fabric', 'Tufted fabric'), ('Tulle', 'Tulle'), ('Tulle', 'Tulle'),
     ('Tusseh silk / Tussah silk', 'Tusseh silk / Tussah silk'),
     ('Tusseh silk / Tussah silk', 'Tusseh silk / Tussah silk'), ('Tweed', 'Tweed'), ('Tweed', 'Tweed'),
     ('Twill', 'Twill'), ('Twill', 'Twill'),
     ('Types of cotton fabric and cotton weave ', 'Types of cotton fabric and cotton weave '),
     ('Types of cotton fabric and cotton weave ', 'Types of cotton fabric and cotton weave '),
     ('Types of knit', 'Types of knit'), ('Types of knit', 'Types of knit'),
     ('Types of satin and satin weave', 'Types of satin and satin weave'),
     ('Types of satin and satin weave', 'Types of satin and satin weave'),
     ('Types of silk fabric and silk weaves', 'Types of silk fabric and silk weaves'),
     ('Types of silk fabric and silk weaves', 'Types of silk fabric and silk weaves'), ('Ultrasuede', 'Ultrasuede'),
     ('Ultrasuede', 'Ultrasuede'), ('Velboa', 'Velboa'), ('Velboa', 'Velboa'), ('Velour', 'Velour'),
     ('Velour', 'Velour'), ('Veloutine', 'Veloutine'), ('Veloutine', 'Veloutine'), ('Velvet', 'Velvet'),
     ('Velvet', 'Velvet'), ('Velveteen', 'Velveteen'), ('Velveteen', 'Velveteen'),
     ('Velveteen plush', 'Velveteen plush'), ('Velveteen plush', 'Velveteen plush'), ('Venecia', 'Venecia'),
     ('Venecia', 'Venecia'), ('Venetian fabric ', 'Venetian fabric '), ('Venetian fabric ', 'Venetian fabric '),
     ('Venice', 'Venice'), ('Venice', 'Venice'), ('Vichy', 'Vichy'), ('Vichy', 'Vichy'), ('Vicuna', 'Vicuna'),
     ('Vicuna', 'Vicuna'), ('Vinyl', 'Vinyl'), ('Vinyl', 'Vinyl'), ('Viscose', 'Viscose'), ('Viscose', 'Viscose'),
     ('Voile', 'Voile'), ('Voile', 'Voile'), ('Wadmal', 'Wadmal'), ('Wadmal', 'Wadmal'),
     ('Waffle cloth', 'Waffle cloth'), ('Waffle cloth', 'Waffle cloth'), ('Washable Paper', 'Washable Paper'),
     ('Washable Paper', 'Washable Paper'), ('Whipcord', 'Whipcord'), ('Whipcord', 'Whipcord'), ('Wincey', 'Wincey'),
     ('Wincey', 'Wincey'), ('Wirecloth', 'Wirecloth'), ('Wirecloth', 'Wirecloth'), ('Wool', 'Wool'), ('Wool', 'Wool'),
     ('Wool crepe', 'Wool crepe'), ('Wool crepe', 'Wool crepe'), ('Woolsy', 'Woolsy'), ('Woolsy', 'Woolsy'),
     ('Worcester', 'Worcester'), ('Worcester', 'Worcester'), ('Worsted ', 'Worsted '), ('Worsted ', 'Worsted '),
     ('Worsted wool', 'Worsted wool'), ('Worsted wool', 'Worsted wool'), ('Yak', 'Yak'), ('Yak', 'Yak'),
     ('Yoryu', 'Yoryu'), ('Yoryu', 'Yoryu'), ('Zanella', 'Zanella'), ('Zanella', 'Zanella'), ('Zephyr', 'Zephyr'),
     ('Zephyr', 'Zephyr'), ('Zibeline', 'Zibeline'), ('Zibeline', 'Zibeline')]

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
