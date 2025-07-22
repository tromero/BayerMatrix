# BayerMatrix
A simple algorithm to generate bayer matrix for ordered dithering. Can output to PNG using PIL. The [PNG files](https://github.com/tromero/BayerMatrix/blob/master/images/) included in this repo should be enough for most use cases.

For dithering, the 16x16 version should produce the best results with the least banding since it has 256 discrete values as opposed to 64 in the 8x8 version.

![16x2](https://github.com/tromero/BayerMatrix/blob/master/images/bayer16tile2.png) 16x16 matrix (tiled 2x)  
![8x4](https://github.com/tromero/BayerMatrix/blob/master/images/bayer8tile4.png) 8x8 matrix (tiled 4x)  
![4x8](https://github.com/tromero/BayerMatrix/blob/master/images/bayer4tile8.png) 4x4 matrix (tiled 8x)  
![2x16](https://github.com/tromero/BayerMatrix/blob/master/images/bayer2tile16.png) 2x2 matrix (tiled 16x)  

[More sizes](https://github.com/tromero/BayerMatrix/tree/master/images)

For reference, here are the numeric values of bayer matrices up to 16x16:

```py
# Bayer Matrix 2
[[0, 2],
[3, 1]]

# Bayer Matrix 4
[[0, 8, 2, 10],
[12, 4, 14, 6],
[3, 11, 1, 9],
[15, 7, 13, 5]]

# Bayer Matrix 8
[[0, 32, 8, 40, 2, 34, 10, 42],
[48, 16, 56, 24, 50, 18, 58, 26],
[12, 44, 4, 36, 14, 46, 6, 38],
[60, 28, 52, 20, 62, 30, 54, 22],
[3, 35, 11, 43, 1, 33, 9, 41],
[51, 19, 59, 27, 49, 17, 57, 25], 
[15, 47, 7, 39, 13, 45, 5, 37],
[63, 31, 55, 23, 61, 29, 53, 21]]

# Bayer Matrix 16
[[0, 128, 32, 160, 8, 136, 40, 168, 2, 130, 34, 162, 10, 138, 42, 170],
[192, 64, 224, 96, 200, 72, 232, 104, 194, 66, 226, 98, 202, 74, 234, 106],
[48, 176, 16, 144, 56, 184, 24, 152, 50, 178, 18, 146, 58, 186, 26, 154],
[240, 112, 208, 80, 248, 120, 216, 88, 242, 114, 210, 82, 250, 122, 218, 90],
[12, 140, 44, 172, 4, 132, 36, 164, 14, 142, 46, 174, 6, 134, 38, 166],
[204, 76, 236, 108, 196, 68, 228, 100, 206, 78, 238, 110, 198, 70, 230, 102],
[60, 188, 28, 156, 52, 180, 20, 148, 62, 190, 30, 158, 54, 182, 22, 150],
[252, 124, 220, 92, 244, 116, 212, 84, 254, 126, 222, 94, 246, 118, 214, 86], 
[3, 131, 35, 163, 11, 139, 43, 171, 1, 129, 33, 161, 9, 137, 41, 169],
[195, 67, 227, 99, 203, 75, 235, 107, 193, 65, 225, 97, 201, 73, 233, 105],
[51, 179, 19, 147, 59, 187, 27, 155, 49, 177, 17, 145, 57, 185, 25, 153],
[243, 115, 211, 83, 251, 123, 219, 91, 241, 113, 209, 81, 249, 121, 217, 89],
[15, 143, 47, 175, 7, 135, 39, 167, 13, 141, 45, 173, 5, 133, 37, 165],
[207, 79, 239, 111, 199, 71, 231, 103, 205, 77, 237, 109, 197, 69, 229, 101],
[63, 191, 31, 159, 55, 183, 23, 151, 61, 189, 29, 157, 53, 181, 21, 149],
[255, 127, 223, 95, 247, 119, 215, 87, 253, 125, 221, 93, 245, 117, 213, 85]]
```
