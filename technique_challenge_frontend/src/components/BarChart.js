import { Bar } from 'vue-chartjs';
import { ChartConfig } from 'Constants/chart-config';

const options = {
  legend: {
    display: false
  },
  tooltips: {
    titleSpacing: 6,
    cornerRadius: 5
  },
  scales: {
    xAxes: [{
      gridLines: {
        display: false,
        color: ChartConfig.chartGridColor,
        drawBorder: false
      },
      ticks: {
        fontColor: ChartConfig.axesColor
      },
      display: false,
    }],
    yAxes: [{
      gridLines: {
        display: false,
        color: ChartConfig.chartGridColor,
        drawBorder: false
      },
      ticks: {
        fontColor: ChartConfig.axesColor,
      },
      display: false
    }]
  }
};

export default {
  extends: Bar,
  props: ['dataSets'],
  watch: {
    dataSets: function(){
      this.rerenderChartMap();
    }
  },
  mounted() {
    this.rerenderChartMap();
  },
  methods: {
    rerenderChartMap: function(){
    const { label, data, labels } = this.dataSets;
    let color = ChartConfig.color.primary;
    this.renderChart({
      labels,
      datasets: [
        {
          barPercentage: 2,
          categoryPercentage: 0.275,
          label: label,
          backgroundColor: color,
          borderColor: color,
          borderWidth: 1,
          hoverBackgroundColor: color,
          hoverBorderColor: color,
          data
        }
      ]
    }, options)
    }
  }
}
