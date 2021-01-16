from PIL import Image, ImageTk
import tkinter as tk
import argparse
import datetime
import cv2
import os



def video_loop():

    global current_image
    """ Get frame from the video stream and show it in Tkinter """
    ok, frame = vs.read()  # read frame from video stream
    if ok:  # frame captured without any errors
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # convert colors from BGR to RGBA
        current_image = Image.fromarray(cv2image)  # convert image for PIL
        imgtk = ImageTk.PhotoImage(image=current_image)  # convert image for tkinter
        panel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
        panel.config(image=imgtk)  # show the image
    root.after(30, video_loop)  # call the same function after 30 milliseconds

def destructor():
    """ Destroy the root object and release all resources """
    print("[INFO] closing...")
    root.destroy()
    vs.release()  # release web camera
    cv2.destroyAllWindows()  # it is not mandatory in this application



def take_snapshot():
    """ Take snapshot and save it to the file """
    # ts = datetime.datetime.now() # grab the current timestamp
    ts = 1
    filename = "{}.jpg".format(ts)  # construct filename
    p = os.path.join(output_path, filename )  # construct output path
    current_image.save(p, "JPEG")  # save image as jpeg file
    print("[INFO] saved {}".format(filename))

def main():
    global vs,output_path,current_image,panel,root
    vs = cv2.VideoCapture(0) # capture video frames, 0 is your default video camera
    output_path = "/home/madan/Desktop/student_managment system/photos"  # store output path
    current_image = None  # current image from the camera
    root = tk.Toplevel()  # initialize root window
    root.title("Camera") 
    panel = tk.Label(root)  # initialize image panel
    panel.pack(padx=10, pady=10)
    btn = tk.Button(root, text="Click", command=lambda:take_snapshot())
    btn.pack(fill="both", expand=True, padx=10, pady=10)
    video_loop()
    print("[INFO] starting...")
    root.mainloop()