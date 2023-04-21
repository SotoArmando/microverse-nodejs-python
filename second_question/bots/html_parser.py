import functools

class HtmlParser():
    def match_attribute(self, tag, classname, attr): 
        """returns a regular expression to match tag & classname while returns a attribute in a group selector"""
        return f"""<{tag}\s+(?:[^>]*?\s+)?class\s*=\s*["']{classname}["'][^>]*?\s+{attr}\s*=\s*["']([^"']+)["'][^>]*?>.*?<\/{tag}>""" 
    
    def match_tag_and_class(self, tag, classname):
        """returns a regular expression to match tag & classname while returns its contents in a group selector"""
        return f"""<{tag}\s+(?:[^>]*?\s+)?class\s*=\s*["']{classname}["'][^>]*?>(.*?)<\/{tag}>'"""
    
    def reduce_matches(self, matches, html):
        """applies regular exprecions on a reduced dict"""
        return functools.reduce(lambda x, key:  {**x, f"{key}": self.reduce_search(matches[key], html) } , matches, {})

    def reduce_search(self, args, html):
        """applies regular exprecions on a reduced single match"""
        return functools.reduce(lambda prev, val:   prev.search(val), args, html) if hasattr(args, "__len__") else html.findall(args)