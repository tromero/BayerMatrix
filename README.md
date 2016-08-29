# BayerMatrix
A simple algorithm to generate bayer matrix for ordered dithering. Can output to PNG using PIL. The [PNG files](https://github.com/tromero/BayerMatrix/blob/master/images/) included in this repo should be enough for most use cases.

For dithering, the 16x16 version should produce the best results with the least banding since it has 256 discrete values as opposed to 64 in the 8x8 version.

![16x2](https://github.com/tromero/BayerMatrix/blob/master/images/bayer16tile2.png) 16x16  
![8x4](https://github.com/tromero/BayerMatrix/blob/master/images/bayer8tile4.png) 8x8  
![4*8](https://github.com/tromero/BayerMatrix/blob/master/images/bayer4tile8.png) 4x4  
![2*16](https://github.com/tromero/BayerMatrix/blob/master/images/bayer2tile16.png) 2x2  
