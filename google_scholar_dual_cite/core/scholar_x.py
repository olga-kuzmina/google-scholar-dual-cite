from google_scholar_dual_cite.core.scholar import ScholarQuery, ScholarConf, ScholarUtils
from urllib import quote


class CitesScholarQuery(ScholarQuery):
    """
    Query for article's cites
    """
    SCHOLAR_CLUSTER_URL = ScholarConf.SCHOLAR_SITE + '/scholar?' \
        + 'cites=%(cluster)s' \
        + '&start=%(start)s' \
        + '&num=%(num)s'

    def __init__(self, cluster, page_num):
        ScholarQuery.__init__(self)
        self.cluster = None
        self.page_num = None
        self.set_cluster(cluster)
        self.set_page_num(page_num)

    def set_cluster(self, cluster):
        """
        Sets search to a Google Scholar results cluster ID.
        """
        msg = 'cluster ID must be numeric'
        self.cluster = ScholarUtils.ensure_int(cluster, msg)

    def set_page_num(self, page_num):
        msg = 'Page number must be numeric'
        self.page_num = ScholarUtils.ensure_int(page_num, msg)

    def get_url(self):
        urlargs = {'cluster': self.cluster,
                   'start': self.page_num * ScholarConf.MAX_PAGE_RESULTS,
                   'num': ScholarConf.MAX_PAGE_RESULTS}

        for key, val in urlargs.items():
            urlargs[key] = quote(str(val))
        return self.SCHOLAR_CLUSTER_URL % urlargs