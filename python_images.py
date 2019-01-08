'''
    About us:
        Youtube Channel: bit.ly/shencshegidzlia
        Facebook Page  : fb.me/shencshegidzlia
        
        შენც შეგიძლია!
        20.05.2018
        
'''

def help_():
    
    result = '''

    ფუნცქია PIL მოდულის გამოყენებით საშუალებას გვაძლევს შევქმნათ ახალი სურათი რამდენიმე სურათის მიმდევრობით გაერთიანებით.
    PIL მოდულის საინსტალაციოდ cmd-ში აკრიფეთ : pip install pillow

    არგუმენტთა მნიშვნელობები:
    
        1. საქაღალდის მისამართი, სადაც გვაქვს შენახული სურათები

        2. საქაღალდის მისამართი, სადაც გვინდა ფუნქციის გამოყენებით შექმნილი სურათის შენახვა

        3. საბოლოო სურათის შემადგენელი პატარა სურათის ზომა პიქსელებში. 
            პრაქტიკულობისა და სიმარტივის მიზნით, მცირე სურათები, რომლებიც ადგენენ საბოლოო სურათს, კვადრატულ ზომას იღებს,
            შესაბამისად, შედეგები არც ისე კარგი შეიძლება იყოს, თუ სურათთა სიგრძესა და სიგანეს შორის დიდი სხვაობაა,
            თუმცა ძირითად შემთხვევებში ეს პრობლემა სავარაუდოდ არაარსებითია.

        4. ჰორიზონტალურად დასამატებელ პატარა სურათთა სასურველი რაოდენობა

        5. ვერტიკალურად დასამატებელ პატარა სურათთა სასურველი რაოდენობა

    '''
    return result

def images_multi(images_folder, save_location, small_image_size, horizontal_number, vertical_number):
    # get information from arguments
    imagesFolder,saveLocation,small_image_dimension, hNum, vNum =  images_folder, save_location, small_image_size, horizontal_number, vertical_number
    #import
    from PIL import Image
    import os, random                 
    # define working variables
    small_image_size = (small_image_dimension, small_image_dimension) # in pixels(image will become square)
    finalSize = ((small_image_dimension * hNum, small_image_dimension * vNum)) # final image size
    background_image = Image.new("RGB", finalSize, (255, 255, 255))            # final image background
    h_position, v_position = 0,0  # starting point
    # print that process started
    print("\n", "| Process Started |".center(70,"*"), "\n", ) 
    # get images list
    imagesList = os.listdir(imagesFolder)
    random.shuffle(imagesList) # make list random
    # do main part
    '''Create list of smaller images, we want to add to final image'''
    resized_image_objects = []
    for index,image_name in enumerate(imagesList):
            image_original = Image.open(os.path.join(imagesFolder,image_name)) #open
            image_resized = image_original.resize(small_image_size) #resize
            resized_image_objects.append(image_resized)     #add to list
            print(str(index + 1).center(4), "|", image_name.ljust(50), " - - - resized ")
            # to not add every single image in this list from folder, we may need much smaller number
            if index == hNum * vNum - 1:
                    break
            
    '''Add smaller images on final image'''       
    #print that second part started
    print("\n", "| Start adding images on final image |".center(70,"="), "\n", )
    #Add smaller images
    for index, image in enumerate(resized_image_objects):	
            background_image.paste(image,(h_position, v_position) ) #paste smaller image
            print(str(index + 1).center(4),"|",imagesList[index].ljust(50), " - - - added") #Print image name (use previous list for this)
            #change horizontal and vertical position, to know where to paste next image
            if index % hNum <  (hNum - 1):
                    h_position += small_image_dimension  #move righter
            else:
                    h_position = 0
                    v_position += small_image_dimension  #move down    

    # save image
    finalImageLocation = os.path.join(saveLocation,"result.jpeg")
    background_image.save(finalImageLocation)  # quality = 100   --> makes image about 5 times bigger in size
    # print
    print("\n", "| Completed! | ".center(60, "*"), "\n")
