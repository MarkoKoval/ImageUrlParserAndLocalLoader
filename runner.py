import picture_parser
import save_images_by_href

local_folder_save = "C:/Users/Acer/Desktop/Calendarimages/"
urls = picture_parser.facade(calendar_flag = "nocal")# can set your parameters (MonthName (lower case), int Year, calendar flag ("cal"/"nocal"), "width*height" )
                                                    # You can try this as width*height parameter 320x480 640x480 800x480 800x600 1024x768 1024x1024 1152x864 1280x800
                                                    # 1280x960 1280x1024 1366x768 1400x1050 1440x900 1600x1200 1680x1050 1680x1200 1920x1440 2560x1440
save_images_by_href.save_images_by_url_locally(urls, local_folder_save)#it saves images to your PC folder using the extracted urls


