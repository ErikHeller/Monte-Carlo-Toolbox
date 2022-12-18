from bokeh.io import output_file, show
from bokeh.plotting import figure

from direct_simulation import ExperimentResults


def repeated_simulation(results: ExperimentResults, out, exact_value=None, title=None, xlog=True,
                        x_axis="Repetitions", y_axis="Value"):
    output_file(out)

    if xlog:
        p = figure(width=800, height=400, x_axis_type="log")
    else:
        p = figure(width=800, height=400)

    trace = results.values[0]  # ToDo: Tuple bug
    repetitions = results.repetitions[0]

    # add a line renderer
    p.line(repetitions, trace, line_width=1, line_color='#4D71D6', legend_label="Simulated value")
    if exact_value:
        p.line(repetitions, [exact_value] * len(repetitions),
               line_width=1, line_color='#FFBE19', line_dash='dashed', legend_label="Exact value")

    if results.confidence_intervals is not None:
        p.varea(x=repetitions, y1=results.confidence_intervals[0], y2=results.confidence_intervals[1],
                level='underlay', fill_alpha=0.2, color='#57BD60',
                legend_label=f"Confidence interval (P>{1-results.confidence_level})")

    diff = abs(max(trace) - min(trace))
    p.y_range.start = min(trace) - diff
    p.y_range.end = max(trace) + diff

    if title:
        p.title.text = title
    p.yaxis.axis_label = y_axis
    p.xaxis.axis_label = x_axis

    show(p)
