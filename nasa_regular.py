import re


def read_file(filename):
    content = None
    try:
        f = open(filename)
        try:
            content = f.read()
            pattern_date = r"	-	(\w+)"
            pattern_url = r"GET	/(\w.+/\w+.\w+)	"
            pattern_code = r"	(\d{3})	"
            date_dict = re.findall(pattern_date, content)
            code_dict = re.findall(pattern_code, content)
            url_dict = re.findall(pattern_url, content)
        finally:
            f.close()

    except FileNotFoundError:
        print("File Nor Found")

    print("pattern_date = " + str(len(date_dict)), "\npattern_url = " + str(len(url_dict)), "\npattern_code = " + str(len(code_dict)))


read_file("nasa_19950801.tsv")