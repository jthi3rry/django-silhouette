from silhouette.templatetags.silhouette_tags import BaseSilhouette, silhouette_tag


@silhouette_tag("mock")
class MockTag(BaseSilhouette):

    def get_extra_context(self):
        ctx = {"obj": self.obj}
        # merge if any "cascaded_*" attributes in context
        attrs = self.merge_attrs(self.cascaded_attrs('cascaded'), self.kwargs)
        # cascade any "cascaded_*" attributes to sub contexts
        attrs = self.build_attrs(attrs, 'cascaded')
        ctx.update(attrs)
        return ctx
