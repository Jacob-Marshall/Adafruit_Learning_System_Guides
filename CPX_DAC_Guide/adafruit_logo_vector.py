### Adafruit logo

"""Adafruit logo created from bitmap,
vectorised and flattened to straight lines by Inkscape
then points extracte from SVG data.
(Other route is to ask Adafruit for vector version!)
"""

### pylint 2.3.1 has some strange opinions on data structure indentation here
### and this conflicts with version 1.9.2
### pylint: disable=invalid-name,bad-continuation
offset_x = -10
offset_y = 9

data = [
        # Removing the box outline
        # Group 1
        #     (2.9962184, 251.49811),
        #     (2.9962184, 1.4981075),
        #     (252.99622, 1.4981075),
        #     (502.99622, 1.4981075),
        #     (502.99622, 251.49811),
        #     (502.99622, 501.49811),
        #     (252.99622, 501.49811),
        #     (2.9962184, 501.49811),
        #     (2.9962184, 251.49811),

        # Outline of the flower followed by the five
        # Group 2
        [(342.49622, 454.21659),
         (346.959242969, 451.054080156),
         (349.16935125, 444.29346125),
         (349.74007, 396.99811),
         (349.42067, 348.99811),
         (346.15117, 331.03534),
         (341.803838594, 322.622872031),
         (336.10557625, 315.17921375),
         (320.50984, 301.96305),
         (315.24595, 297.9209),
         (322.89745, 300.16203),
         (338.78867125, 303.15162),
         (354.51274, 302.19987),
         (370.1502025, 297.314415),
         (383.99038, 290.42349),
         (425.3782575, 261.03182375),
         (455.62553, 237.51598),
         (457.673981406, 232.384370781),
         (457.63498125, 226.75574125),
         (455.656955469, 221.435746094),
         (451.88833, 217.23004),
         (411.03035375, 203.142875),
         (364.28838, 189.00345),
         (346.28838, 187.51289),
         (334.345396094, 188.212601406),
         (324.08682875, 190.43598375),
         (314.755874531, 194.422959219),
         (305.59573, 200.41345),
         (298.69523, 205.64576),
         (302.36566, 200.82194),
         (309.1910175, 190.60812125),
         (313.73687, 180.22634),
         (316.80698125, 162.25769875),
         (315.61122, 142.49811),
         (302.2062, 97.30761225),
         (287.72529, 54.616095),
         (281.9467975, 48.27558525),
         (273.17468, 46.774785),
         (268.19440125, 47.74447575),
         (264.37486, 50.652804),
         (236.2211725, 88.324987),
         (209.53225, 127.99811),
         (202.6606625, 146.3071125),
         (201.25938, 164.93584),
         (203.77534, 181.49811),
         (206.51089, 188.99811),
         (205.9051675, 188.794985),
         (203.43769, 185.49811),
         (196.64267375, 177.104034375),
         (188.75523, 169.97381),
         (179.92702375, 164.224298125),
         (170.30972, 159.97236),
         (160.326935313, 157.051098125),
         (148.6087275, 155.3990125),
         (102.61522, 154.49966),
         (60.16592325, 155.3425225),
         (53.6551856875, 157.376749063),
         (50.290496, 161.35986),
         (47.372345, 168.60014),
         (48.89669, 175.71523),
         (74.532052, 211.99811),
         (94.1360167813, 237.819985),
         (108.59780025, 254.2254825),
         (120.832361594, 264.08215625),
         (133.75466, 270.25756),
         (141.60613, 272.36428),
         (152.49621, 273.38038),
         (164.49621, 273.99811),
         (158.0089, 275.81829),
         (145.07552625, 280.9514125),
         (133.8165275, 288.7022225),
         (124.0311775, 299.24521125),
         (115.51875, 312.75487),
         (98.843153625, 358.473565),
         (85.295136, 403.16722),
         (85.26685925, 408.01758375),
         (86.915068, 411.86681),
         (92.4915405, 417.39844125),
         (99.473822, 419.49811),
         (143.00896275, 406.315715),
         (190.36777, 389.38911),
         (202.01838, 382.636295),
         (212.26301, 373.79104),
         (221.50430875, 362.505715),
         (227.61924, 348.61117),
         (230.74226, 339.12239),
         (231.21585, 351.56025),
         (232.0963625, 362.919155),
         (234.30307, 370.76155),
         (242.12680375, 385.41184875),
         (253.38592, 399.00254),
         (289.43734875, 427.02384125),
         (327.49622, 454.1789),
         (334.9740875, 456.36105375),
         #(342.49622, 454.2166),
         #(342.49622, 454.21659),
        ],
        # Group 3
        [(269.38148, 328.24811),
         (260.235962344, 318.54971125),
         (252.98225875, 304.9253925),
         (249.221025781, 291.33056),
         (249.150290957, 285.780265547),
         (250.55292, 281.72062),
         (254.134922402, 279.408903848),
         (258.744026719, 280.396155156),
         (263.916454863, 284.085617324),
         (269.18842875, 289.88053375),
         (278.175901406, 305.399702969),
         (280.963844004, 313.930442559),
         (281.99622, 322.17961),
         (281.55819875, 326.77132),
         (279.99622, 329.49811),
         (275.74986, 331.3257375),
         #(269.38148, 328.24811),
         #(269.38148, 328.24811),
        ],
        # Group 4
        [(189.27613, 317.48919),
         (186.689292012, 315.017226172),
         (186.253231719, 310.95217),
         (190.75285125, 299.8028675),
         (200.613802656, 287.56145625),
         (213.6749, 277.74811),
         (220.431676309, 274.964493711),
         (225.392900469, 274.551332812),
         (228.531887832, 276.197175508),
         (229.82195375, 279.59057),
         (229.236413574, 284.420064492),
         (226.748582656, 290.374207187),
         (215.95931, 304.41063),
         (208.563450625, 310.792326562),
         (201.1146375, 315.3621975),
         (194.417365625, 317.725924687),
         #(189.27613, 317.48919),
         #(189.27613, 317.48919),
        ],
        # Group 5
        [(270.49622, 263.99178),
         (266.275620215, 261.866190078),
         (264.014989219, 259.301005),
         (263.608503301, 256.443141797),
         (264.95033875, 253.4395175),
         (272.455678906, 247.58265375),
         (285.68442, 242.90575),
         (302.642775, 241.59651875),
         (316.00365, 244.06329),
         (319.7235275, 248.4713),
         (318.6949, 253.83523),
         (310.640874688, 259.620080625),
         (297.3441375, 263.7845675),
         (282.673111563, 265.513523125),
         #(270.49622, 263.99178),
         #(270.49622, 263.99178),
        ],
        # Group 6
        [(202.04337, 252.52942),
         (191.235123437, 247.592305),
         (181.9467875, 241.23868),
         (175.444952812, 234.5173375),
         (172.99621, 228.47707),
         (174.24765832, 224.997173086),
         (177.684219687, 223.036961563),
         (189.20598, 223.281585),
         (203.748087812, 228.422920938),
         (217.49714, 237.67295),
         (224.516762344, 246.891496563),
         (224.975280254, 250.442414727),
         (223.57588375, 253.118295),
         (220.450783652, 254.792036523),
         (215.732190781, 255.336538437),
         #(202.04337, 252.52942),
         #(202.04337, 252.52942),
        ],
        # Group 7
        [(243.14004, 239.17141),
         (240.444360469, 233.682861094),
         (238.94700375, 225.78207875),
         (239.96685, 206.99811),
         (245.63492375, 191.82701),
         (249.349385156, 186.715313438),
         (252.99622, 184.38871),
         (256.799735, 184.899581563),
         (259.7174025, 187.9743),
         (262.71503, 201.49811),
         (261.901079688, 215.476273438),
         (258.45465, 228.0064775),
         (253.205227813, 237.032497812),
         (250.16360918, 239.588868945),
         (246.9823, 240.49811),
         #(243.14004, 239.17141),
         #(243.14004, 239.17141),
        ]
       ]