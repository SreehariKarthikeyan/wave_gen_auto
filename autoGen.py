'''
A Simple program to automate wave runs with different seed values.
Requirements:
1.OpenCV
2.pywinauto
3.pyautogui
4.pynput
5.functools
Create a conda env with the requirements.txt file provided

Images under software_images are required to run this script.
Note: This is a sensitive and linear script, do not interrupt the program or use mouse/keyboard during the script run. To end the script in the middle press esc twice.
'''

import sys
import pyautogui
import pywinauto,time
from pywinauto.application import Application
import _thread
from pynput import keyboard
from functools import wraps

space='D:/Personel Projects/WavaGenAuto/'    #Change to Project Location
SOFTWARE_PATH=r"E:\edesign\bin\WaveSynthesiserAuto.exe" #Chnage to Software .exe Location

NEW_EXPERIMENT='software_images/new-experiment.png'
CREATE_BLANK_WAVE='software_images/create_a_blank_wave.png'
OK_BUTTON='software_images/ok_button_1.png'
YES_BUTTON='software_images/yes-button.png'
DEFAULT_VALUE_BUTTON='software_images/default-value-button.png'
ADD_BUTTON='software_images/add-button.png'
DELETE_BUTTON='software_images/delete-button.png'
CLOSE_BUTTON='software_images/close-button.png'
WAVE_SPEC_BUTTON='software_images/wave_spec.png'
WAVE_TEMPLATE_CREATE_BUTTON='software_images/wave-template-create.png'
WAVE_DEF_CHECKBOX='software_images/wave-def-check.png'
WAVE_SPEC_CHECKBOX='software_images/wave-spec-check.png'
JOHN_SWAP_CHECKBOX='software_images/john-swap-check.png'
RANDOM_CHECKBOX='software_images/random-check.png'
WAVE_RUNS_BUTTON='software_images/wave-runs.png'
CREATE_TEMPLATE_WAVE='software_images/create_wave_from_temp.png'
SELECT_SIMPLE_SINE_WAVE='software_images/simple-sne-wave-select.png'
SELECT_JOHN_SWAP='software_images/john-swap-select.png'
SELECT_RANDOM_WAVE='software_images/random-select.png'
JOHN_SWAP_Y='software_images/john-swap-yellow.png'
TEMPLATE_BUTTON='software_images/templates-button.png'
CREATE_SINE_WAVE_DEFAULT ='software_images/simple-sine-wave-default.png'
SIMPLE_SPECTRUM_DEFAULT='software_images/simple_spectrum_template.png'
SELECTED_WAVE='software_images/selected_wave_opt.png'
SAVE_DATA_TO_FILE='software_images/save-data-to-file.png'
OK_BUTTON_SAVE='software_images/ok_button_2.png'

def program_terminator(
    start_message="",
    end_message="",
    keyboard_key=keyboard.Key.esc,
    key_string="Esc",
):
   
    def _decorate(func):
        def _keyboard_handler(key, escape_key=keyboard_key):
            if key == escape_key:
                print("Program terminated by user")
                _thread.interrupt_main()

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Handle keyboard interrupts by user
            with keyboard.Listener(on_press=_keyboard_handler):
                print(start_message)
                print(
                    f" Press '{key_string}' any time to terminate the program",
                )
                # Do inner function
                result = func(*args, **kwargs)

            return result

        return wrapper

    return _decorate


def _create_template(_experiment_name,_template_name):
    '''creates a template with default specs'''
    pyautogui.rightClick(pyautogui.locateOnScreen(WAVE_SPEC_BUTTON,confidence=0.9))
    pyautogui.hotkey("down")
    pyautogui.press('enter')

    for i in range(0,2):
        pyautogui.hotkey("down")

    pyautogui.press('enter')

    for i in range(0,5):
        pyautogui.hotkey("down")
    pyautogui.press('enter')

    
    time.sleep(1)
    pyautogui.rightClick(pyautogui.locateOnScreen(WAVE_SPEC_BUTTON,confidence=0.9))
    pyautogui.hotkey("down")
    pyautogui.press('enter')

    for i in range(0,8):
        pyautogui.hotkey("down")
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey("up")
    pyautogui.press('enter')
    pyautogui.click(pyautogui.locateOnScreen(WAVE_TEMPLATE_CREATE_BUTTON,confidence=0.9))
    time.sleep(1)
    
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey("backspace")
   
    pyautogui.typewrite(_template_name)

    def _monotonous(_click_button,_pt_value):
        pyautogui.click(_click_button)
        pyautogui.move(_pt_value, 0)   
        pyautogui.click()


    wave_def_check=pyautogui.locateOnScreen(WAVE_DEF_CHECKBOX,confidence=0.9)
    _monotonous(wave_def_check,-58)

    wave_spec_check=pyautogui.locateOnScreen(WAVE_SPEC_CHECKBOX,confidence=0.9)
    _monotonous(wave_spec_check,-54)
    pyautogui.move(-10, 0)   
    pyautogui.click()

    john_swap_check=pyautogui.locateOnScreen(JOHN_SWAP_CHECKBOX,confidence=0.9)
    _monotonous(john_swap_check,-54)

    random_check=pyautogui.locateOnScreen(RANDOM_CHECKBOX,confidence=0.9)
    _monotonous(random_check,-29)
    pyautogui.click(pyautogui.locateOnScreen(OK_BUTTON,confidence=0.9))
    
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey("backspace")

    pyautogui.typewrite(_experiment_name)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(pyautogui.locateOnScreen(YES_BUTTON,confidence=0.9))
    time.sleep(1.5)
    pyautogui.click(pyautogui.locateOnScreen(CLOSE_BUTTON,confidence=0.9))
    pyautogui.click(pyautogui.locateOnScreen(CLOSE_BUTTON,confidence=0.9))
    time.sleep(1.5)


def _add_default_value():
    '''adds default gamma value'''
    pyautogui.hotkey('ctrl', 'p') 
    time.sleep(1)
    pyautogui.click(pyautogui.locateOnScreen(DEFAULT_VALUE_BUTTON,confidence=0.9))
    pyautogui.click(pyautogui.locateOnScreen(ADD_BUTTON,confidence=0.9))
    time.sleep(1)
    for i in range(0,2):
        pyautogui.typewrite('gamma')
        pyautogui.hotkey("tab")
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey("backspace")
    pyautogui.typewrite('1')
  
    pyautogui.click(pyautogui.locateOnScreen(OK_BUTTON,confidence=0.9))
    time.sleep(1.5)
    pyautogui.click(pyautogui.locateOnScreen(CLOSE_BUTTON,confidence=0.9))
    time.sleep(1.5)


def _generate_waves_for_n_seed(_experiment_name,_template_name,max_seed,hs_val='0.8',tp_val='0.5',seed_start_value=2):
        '''runs the script for n loops'''
       
        for i in range(0,int(max_seed)):
            pyautogui.rightClick(pyautogui.locateOnScreen(WAVE_RUNS_BUTTON,confidence=0.9))

            for i in range(0,2):
                pyautogui.hotkey("down")
                pyautogui.press('enter')

            #create new runs
            pyautogui.click(pyautogui.locateOnScreen(CREATE_TEMPLATE_WAVE,confidence=0.9))
            pyautogui.click(pyautogui.locateOnScreen(SELECT_SIMPLE_SINE_WAVE,confidence=0.9))
        
            pyautogui.typewrite(_template_name[0])
            time.sleep(1)
            pyautogui.click(pyautogui.locateOnScreen(OK_BUTTON,confidence=0.9))

            #select wave spec values
            pyautogui.click(pyautogui.locateOnScreen(SELECT_JOHN_SWAP,confidence=0.9))
        
            for i in range(0,4):
                pyautogui.hotkey("tab")

            pyautogui.typewrite(hs_val)

            for i in range(0,3):
                pyautogui.hotkey("tab")
            pyautogui.typewrite(tp_val)

            for i in range(0,3):
                pyautogui.hotkey("tab")
            pyautogui.typewrite('1')

            pyautogui.click(pyautogui.locateOnScreen(SELECT_RANDOM_WAVE,confidence=0.9))
            time.sleep(1)
            for i in range(0,5):
                pyautogui.hotkey("tab")
            pyautogui.typewrite('{0}'.format(seed_start_value))      
            time.sleep(1)
            pyautogui.click(pyautogui.locateOnScreen(JOHN_SWAP_Y,confidence=0.9))
        
            pyautogui.click(pyautogui.locateOnScreen(SAVE_DATA_TO_FILE,confidence=0.9))
            time.sleep(1)
                 
            pyautogui.click(pyautogui.locateOnScreen(OK_BUTTON_SAVE,confidence=0.5))
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey("backspace")
            pyautogui.typewrite('{0}_seed_{1}'.format(_experiment_name,seed_start_value))
            pyautogui.press('enter')
            seed_start_value=seed_start_value+1
            time.sleep(1)
            
def _destroy_template(_template_name):
    pyautogui.hotkey('ctrl', 'p') 
    time.sleep(1)
    pyautogui.click(pyautogui.locateOnScreen(TEMPLATE_BUTTON,confidence=0.9))
   
    pyautogui.click(pyautogui.locateOnScreen(SIMPLE_SPECTRUM_DEFAULT,confidence=0.9))
    init_pt=pyautogui.position()
    pyautogui.typewrite(_template_name[0])  
    # pyautogui.click(pyautogui.locateOnScreen(SELECTED_WAVE,confidence=0.9))
    # move_pt=pyautogui.position()
    # print(move_pt[0])
    # time.sleep(1)
    # if (init_pt[0]!=move_pt[0]):
    #     pyautogui.click(pyautogui.locateOnScreen(DELETE_BUTTON,confidence=0.9))
    pyautogui.click(pyautogui.locateOnScreen(DELETE_BUTTON,confidence=0.9))
    pyautogui.click(pyautogui.locateOnScreen(CLOSE_BUTTON,confidence=0.9))

@program_terminator(start_message="program terminator initiated", end_message="Program Ended by user")
def main(path=SOFTWARE_PATH):
    '''main driver function'''
    _experiment_name=input('Enter Experiment Name:')
    _template_name=input('Enter Template Name:')
    _max_seed_value=input('Enter Number of runs(seed):')
    if len(_max_seed_value)==0:
        print('Provide Seed Value!')
        sys.exit()
    _hsValue=input('Enter Hs value:')
    _tpValue=input('Enter Tp value:')

    app=Application('uia').start(cmd_line=path).connect(title='Njörðr Wave Synthesis',timeout=100)   
    time.sleep(1)
    try:
        pyautogui.click(pyautogui.locateOnScreen(NEW_EXPERIMENT,confidence=0.5))
        # pyautogui.press('enter') #optional
        pyautogui.typewrite(_experiment_name)
        pyautogui.hotkey("tab")

        for  i in range(0,4):
            pyautogui.hotkey("down")

        pyautogui.hotkey("tab")
        pyautogui.press('enter')

        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey("backspace")
        pyautogui.typewrite('Run 1')
        pyautogui.click(pyautogui.locateOnScreen(CREATE_BLANK_WAVE,confidence=0.9))
        pyautogui.click(pyautogui.locateOnScreen(OK_BUTTON,confidence=0.9))
        time.sleep(1)
        # seed_value=2

        _add_default_value()
        _create_template(_experiment_name,_template_name)
        if((len(_hsValue)==0) & (len(_tpValue)==0)):
            _generate_waves_for_n_seed(_experiment_name,_template_name,_max_seed_value)
        else:
            _generate_waves_for_n_seed(_experiment_name,_template_name,_max_seed_value,_hsValue,_tpValue)
        
    except  Exception as e:    
        print(e)
        pyautogui.alert('Something went wrong. Restart the program')
        sys.exit()
    finally :
        time.sleep(2)
        _destroy_template(_template_name)
        pyautogui.alert('Wave generated for {0} seed values'.format(_max_seed_value))

if __name__=='__main__':    
    main()



