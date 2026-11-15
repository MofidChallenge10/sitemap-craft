#!/usr/bin/env python3
"""Generate a sitemap.xml from HTML files in a static site directory."""
import argparse,datetime as dt,pathlib,sys,unittest,xml.etree.ElementTree as ET
from urllib.parse import quote,urljoin
NS="http://www.sitemaps.org/schemas/sitemap/0.9"
def build(root,base_url):
    root=pathlib.Path(root).resolve(); base=base_url.rstrip("/")+"/"
    urlset=ET.Element(f"{{{NS}}}urlset")
    for file in sorted(root.rglob("*.html")):
        rel=file.relative_to(root)
        if any(part.startswith(".") for part in rel.parts): continue
        loc=urljoin(base,quote(rel.as_posix()))
        modified=dt.datetime.fromtimestamp(file.stat().st_mtime,dt.timezone.utc).date().isoformat()
        item=ET.SubElement(urlset,f"{{{NS}}}url"); ET.SubElement(item,f"{{{NS}}}loc").text=loc
        ET.SubElement(item,f"{{{NS}}}lastmod").text=modified
    return ET.tostring(urlset,encoding="unicode",xml_declaration=True)
class Tests(unittest.TestCase):
    def test_hidden_excluded_and_url_encoded(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root=pathlib.Path(tmp); (root/"index.html").write_text("x"); (root/"a b.html").write_text("x")
            (root/".hidden").mkdir(); (root/".hidden"/"no.html").write_text("x")
            xml=build(root,"https://example.test"); self.assertIn("a%20b.html",xml); self.assertNotIn(".hidden",xml)
    def test_empty(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp: self.assertIn("urlset",build(tmp,"https://e.test"))
def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("root"); ap.add_argument("base_url"); ap.add_argument("-o","--output",default="sitemap.xml"); a=ap.parse_args()
    try: xml=build(a.root,a.base_url); pathlib.Path(a.output).write_text(xml+"\n",encoding="utf-8")
    except OSError as exc: ap.error(str(exc))
    print(f"Wrote {a.output}")
if __name__=="__main__":
    if "--self-test" in sys.argv: unittest.main(argv=[sys.argv[0]])
    else: main()
