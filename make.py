import Image
import sys

W, H = 0, 1

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print "%s WIDTH HEIGHT" % (sys.argv[0])
        sys.exit(1)
    try:
        width, height = int(sys.argv[1]), int(sys.argv[2])
    except:
        print "%s WIDTH HEIGHT" % (sys.argv[0])
        sys.exit(1)

    # Destination canvas
    canvas = Image.new("RGB", (width, height))
    # Open elements
    for time in ["midnight", "2am", "314am", "4am", "6am", "8am", "10am",
                 "noon", "2pm", "4pm", "6pm", "8pm", "10pm"]:
        # Open source files
        headertile_bg = Image.open("field/%s/headertile_bg.jpg" % time)
        footer_bg_rside = Image.open("field/%s/footer_bg_rside.jpg" % time)
        footertile_bg_rside = Image.open("field/%s/footertile_bg_rside.jpg" % time)
        canvastile_bg = Image.open("field/%s/canvastile_bg.jpg" % time)

        # Top
        for i in range(width / headertile_bg.size[W] + 1):
            canvas.paste(headertile_bg, (i * headertile_bg.size[W], 0))

        # Overlap top and bottom
        for i in range(width / canvastile_bg.size[W] + 1):
            overlap_height = height - headertile_bg.size[H] - footertile_bg_rside.size[H]
            for j in range(overlap_height / canvastile_bg.size[H] + 1):
                x = i * canvastile_bg.size[W]
                y = j * canvastile_bg.size[H] + headertile_bg.size[H]
                canvas.paste(canvastile_bg, (x, y))


        # Bottom left tiles - start by slight overlap
        tile_end = width - footer_bg_rside.size[W] + 120
        tile_start = tile_end
        # Go left
        while(tile_end > 0):
            x = tile_end - footertile_bg_rside.size[W]
            y = height - footertile_bg_rside.size[H]
            canvas.paste(footertile_bg_rside, (x, y))
            tile_end -= footertile_bg_rside.size[W]
        # Go right
        while(tile_start < width):
            x = tile_start
            y = height - footertile_bg_rside.size[H]
            canvas.paste(footertile_bg_rside, (x, y))
            tile_start += footertile_bg_rside.size[W]

        # Lower right
        canvas.paste(footer_bg_rside, (width - footer_bg_rside.size[W],
                                       height - footer_bg_rside.size[H]))
        

        canvas.save("teahouse_%s.jpg" % time)
