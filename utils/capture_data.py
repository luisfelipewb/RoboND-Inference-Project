import cv2

cap = cv2.VideoCapture(0)
name_type = 'nothing'
set_dir = 'nothing'
i = 1

print ("Photo capture enabled! 'enter' to take photos, 'esc' to exit.")

while True:

    # Read in and display frame from webcam
    ret, frame = cap.read()
    cv2.imshow('Color Picture', frame)


    # Use 'enter' to take picture
    if cv2.waitKey(1) & 0xFF == 13:
	# Original image size is 1280x720, crop square in the center and resize
       	image = frame[:,280:1000]
        image = cv2.resize(image,(256,256), interpolation = cv2.INTER_NEAREST)
 
	# Save image
	number = "%04d" % (i,)
	dir = 'data/' + set_dir + '/'
	filename = name_type + "_" + str(number) + ".png"
	cv2.imwrite(dir + filename,image)
        #cv2.imwrite('data/' + set_dir + '/' + name_type + "_" + str(number) + ".png", image)
	print ("Saving image: " + filename)
        i += 1

    # Press 'b' to change to beaglebone
    if cv2.waitKey(1) & 0xFF == 98:
        name_type = 'beaglebone'
        set_dir = 'beaglebone'
        i = 1
	print ("Changed to taking pictures of 'beaglebone'")

    # Press 'c' to change to cube 
    if cv2.waitKey(1) & 0xFF == 99:
        name_type = 'cube'
        set_dir = 'cube'
        i = 1
	print ("Changed to taking pictures of 'cube'")

    # Press 'esc' to quit the program
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
