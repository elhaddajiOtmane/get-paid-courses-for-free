from urllib.parse import quote

def format_url(course_name, year, month):
    # Remove colons from the course name
    formatted_course_name = course_name.replace(':', '')

    # Encode the course name for URL compatibility
    encoded_course_name = quote(formatted_course_name, safe='')

    # Replace spaces with %20 for URL encoding
    encoded_course_name = encoded_course_name.replace(' ', '%20')

    # Format the URL
    url = f"https://freecoursesite.com/wp-content/uploads/{year}/{month}/FreeCourseSite.com-Udemy%20-%20{encoded_course_name}.torrent"

    return url

# Example usage
course_name = input("Enter the course name: ")
year = input("Enter the year: ")
month = input("Enter the month: ")

url = format_url(course_name, year, month)
print("Formatted URL:", url)
