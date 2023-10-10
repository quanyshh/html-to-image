import os
from html2image import Html2Image

hti = Html2Image(output_path='images') #size=(500, 200)

if not os.path.exists('images'):
    os.mkdir('images')

css = "{background: white;}"

def main(files_dir):
    html_files_list = os.listdir(files_dir)
    for file in html_files_list:
        html_path = f'{files_dir}/{file}'
        image_path = f'{os.path.basename(file)}.png'

        hti.screenshot(
            html_file=html_path,
            css_str=css,
            save_as=image_path
        )
    print(html_files_list)

if __name__ == '__main__':
    main(files_dir = 'files')