from django.template.loader import render_to_string


def disqus_block_html(disqus_username):
    print("Showing disqus")
    print(render_to_string("disqusblock.html", context={"disqus_username": disqus_username}))
    return render_to_string("disqusblock.html", context={"disqus_username": disqus_username})