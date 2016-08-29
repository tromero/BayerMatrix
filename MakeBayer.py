def InitBayer(x, y, size, value, step,
              matrix = [[]]):
    if matrix == [[]]:
        matrix = [[0 for i in range(size)]for i in range(size)]
    
    if (size == 1):
        matrix[y][x] = value
        return
    
    half = size/2
    
    #subdivide into quad tree and call recursively
    #pattern is TL, BR, TR, BL
    InitBayer(x,      y,      half, value+(step*0), step*4, matrix)
    InitBayer(x+half, y+half, half, value+(step*1), step*4, matrix)
    InitBayer(x+half, y,      half, value+(step*2), step*4, matrix)
    InitBayer(x,      y+half, half, value+(step*3), step*4, matrix)
    return matrix

def MakeBayer(matrixSize, savePng, pngTileCount):
    pngFilename = 'bayer%d.png' % matrixSize
    if (pngTileCount > 1):
        pngFilename = 'bayer%dtile%d.png' % (matrixSize, pngTileCount)

    matrix = InitBayer(0, 0, matrixSize, 0, 1)
    
    if (savePng):
        from PIL import Image
        brightnessMultiplier = {16:1,8:4,4:16,2:64}
        img = Image.new('RGB', (matrixSize*pngTileCount,
                                matrixSize*pngTileCount))
        imgData = img.load()
        for y in range(img.height):
            for x in range(img.width):
                value = matrix[y % matrixSize][x % matrixSize]
                value *= brightnessMultiplier[matrixSize]
                color = (value, value, value)
                imgData[x,y] = color
        img.save(pngFilename, "PNG")
        print('Saved %s' % pngFilename)
    else:
        print('Bayer Matrix %s' % matrixSize)
        print(matrix)


if __name__ == '__main__':
    # size should be a power of two.
    # note that matrix sizes larger than 16 go out of 0..255 range,
    # so image export will not work correctly
    sizes = 2,4,8,16
    
    tileCounts = 1,2,4,8,16

    for size in sizes:
        for tileCount in tileCounts:
            MakeBayer(matrixSize=size, savePng=True, pngTileCount=tileCount)
