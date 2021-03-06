import _plotly_utils.basevalidators


class SideValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='side', parent_name='layout.xaxis', **kwargs
    ):
        super(SideValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot+margins',
            role='info',
            values=['top', 'bottom', 'left', 'right'],
            **kwargs
        )
