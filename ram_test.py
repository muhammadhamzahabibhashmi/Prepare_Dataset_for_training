import pyvista as pv
import cv2
import time
import os

rot_array = []
rot1_array = []
mesh = pv.read('models/male_logo.obj')
mesh.texture_map_to_plane(inplace=True)
qwe1 = pv.read_texture('models/black.jpg')
mesh1 = pv.read("models/avtar.obj")
mesh1.texture_map_to_plane(inplace=True)
for idx in range(900):
    rot_array.append(mesh1.rotate_y(0.5 * idx, inplace=False))  # point=axes.origin
    rot1_array.append(mesh.rotate_y(0.5 * idx, inplace=False))  # point=axes.origin
    print(idx)


def build_model_m(i):
    folder = str(i)
    try:
        os.mkdir(folder)
    except:
        print("done_already")

    print("aa")
    p = pv.Plotter()  # BackgroundPlotter()

    p.open_movie(str(i) + "m" + '.mp4', quality=8)
    vidcap = cv2.VideoCapture('vidtex1/' + str(i) + ".mp4")

    for m in range(1800):

        p.clear()
        success, image = vidcap.read()
        if success:
            cv2.imwrite(folder + '/' + str(m) + '.jpg', image)
            qwe = pv.read_texture(folder + '/' + str(m) + '.jpg')
            p.add_background_image('models/black.jpg')
            p.add_mesh(rot_array[m], texture=qwe)
            p.add_mesh(rot1_array[m], texture=qwe1)
            p.view_xy()
            p.write_frame()
            p.remove_background_image()
    p.close()
    i = i + 1


start = time.time()
build_model_m(6)
print("time taken: " + str((time.time() - start)))