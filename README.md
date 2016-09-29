# BayerMatrix
A simple algorithm to generate bayer matrix for ordered dithering. Can output to PNG using PIL. The [PNG files](https://github.com/tromero/BayerMatrix/blob/master/images/) included in this repo should be enough for most use cases.

For dithering, the 16x16 version should produce the best results with the least banding since it has 256 discrete values as opposed to 64 in the 8x8 version.

![16x2](https://github.com/tromero/BayerMatrix/blob/master/images/bayer16tile2.png) 16x16 matrix (tiled 2x)  
![8x4](https://github.com/tromero/BayerMatrix/blob/master/images/bayer8tile4.png) 8x8 matrix (tiled 4x)  
![4x8](https://github.com/tromero/BayerMatrix/blob/master/images/bayer4tile8.png) 4x4 matrix (tiled 8x)  
![2x16](https://github.com/tromero/BayerMatrix/blob/master/images/bayer2tile16.png) 2x2 matrix (tiled 16x)  

[More sizes](https://github.com/tromero/BayerMatrix/tree/master/images)
