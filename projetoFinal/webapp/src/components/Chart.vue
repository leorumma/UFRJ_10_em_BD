<template>
  <b-card :title="chartLabel">
    <b-card-text>
      <canvas :id="`chart${item}`"/>
    </b-card-text>
  </b-card>
</template>

<script>
import Chart from 'chart.js'

export default {
  name: 'chart',

  props: {
    // para diferenciar cada grafico se existir vários
    // em uma mesma página.
    item: {
      type: Number,
      required: true
    },

    // tipo de grafico a ser desenhado, ex: bar, line, pie, etc
    // referencia para os tipos possiveis: https://www.chartjs.org/docs/latest/charts/
    chartType: {
      type: String,
      required: true
    },

    // label que ficará no card do gráfico
    chartLabel: {
      type: String,
      required: false
    },

    // dados do grafico. deve ser um array de objetos com o label de cada dado que possuir
    data: {
      type: [Array, Object],
      required: true
    },

    // nome da propriedade que possui o label dentro do objeto de array de dados.
    // por padrão é 'label'
    dataLabelProp: {
      type: String,
      required: false,
      default: 'label'
    },

    // nome da propriedade que possui o valor do dado dentro do objeto de array de dados.
    // por padrão é 'value'
    dataValueProp: {
      type: String,
      required: false,
      default: 'value'
    },

    showLegend: {
      type: Boolean,
      required: false,
      default: true
    }
  },

  // desenha o gráfico quando o componente pai recebe os dados da api e modifica
  // o array de dados. necessario por causa da assincronicidade
  watch: {
    'data': function () {
      this.createChart(`chart${this.item}`)
    }
  },

  // desenha o grafico quando o usuario acessa a pagina dos graficos
  // não é necessário porque quando ele acessa, a página não possui os
  // os dados ainda mas vai que né
  mounted () {
    this.createChart(`chart${this.item}`)
  },

  methods: {
    // inicializa os dados referentes ao grafico
    initChartDataForBar () {
      let arrayColors = ['#FF6384', '#FF9F40', '#36A2EB', '#4BC0C0', '#FFCD56', '#835EA2']

      let chart = {
        labels: [],
        datasets: [{
          label: this.chartLabel,
          data: [],
          borderWidth: 3,
          backgroundColor: []
        }]
      }

      for (const [index, data] of this.data.entries()) {
        if (!data[this.dataLabelProp]) {
          console.error(`O objeto do dado não possui ${this.dataLabelProp} para o label.`)
        }

        if (!data[this.dataValueProp]) {
          console.error(`O objeto do dado não possui ${this.dataValueProp} para o value.`)
        }

        chart.labels.push(data[this.dataLabelProp])

        chart.datasets[0].data.push(data[this.dataValueProp])

        chart.datasets[0].backgroundColor.push(arrayColors[index % arrayColors.length])
      }

      return chart
    },

    initChartDataForStackedBar () {
      let arrayColors = ['#FF6384', '#4BC0C0', '#FFCD56', '#FF9F40', '#36A2EB']

      let chart = {
        labels: this.data.labels,
        datasets: []
      }

      for (const [index, dataset] of this.data.datasets.entries()) {
        chart.datasets.push({
          label: dataset.label,
          data: dataset.data,
          borderWidth: 3,
          backgroundColor: arrayColors[index % arrayColors.length]
        })
      }

      return chart
    },

    initChartDataForPie () {
      let arrayColors = ['#FF6384', '#FF9F40', '#36A2EB', '#4BC0C0', '#FFCD56', '#835EA2']

      let chart = {
        labels: [],
        datasets: [{
          label: this.chartLabel,
          data: [],
          borderWidth: 3,
          backgroundColor: []
        }]
      }

      for (const [index, data] of this.data.entries()) {
        if (!data[this.dataLabelProp]) {
          console.error(`O objeto do dado não possui ${this.dataLabelProp} para o label.`)
        }

        if (!data[this.dataValueProp]) {
          console.error(`O objeto do dado não possui ${this.dataValueProp} para o value.`)
        }

        chart.labels.push(data[this.dataLabelProp])

        chart.datasets[0].data.push(data[this.dataValueProp])

        chart.datasets[0].backgroundColor.push(arrayColors[index % arrayColors.length])
      }

      return chart
    },

    initChartDataForLine () {
      let chart = {
        labels: [],
        datasets: [{
          label: this.chartLabel,
          data: [],
          borderWidth: 3,
          borderColor: '#835EA2',
          fill: false
        }]
      }

      for (let data of this.data) {
        if (!data[this.dataLabelProp]) {
          console.error(`O objeto do dado não possui ${this.dataLabelProp} para o label.`)
        }

        if (!data[this.dataValueProp]) {
          console.error(`O objeto do dado não possui ${this.dataValueProp} para o value.`)
        }

        chart.labels.push(data[this.dataLabelProp])

        chart.datasets[0].data.push(data[this.dataValueProp])
      }

      return chart
    },

    // função para desenhar o grafico
    createChart (chartId) {
      if (this.data && this.data.length === 0) {
        return
      }

      let chartType, chartData, chartOptions

      if (this.chartType === 'stacked bar') {
        chartType = 'bar'
        chartData = this.initChartDataForStackedBar()
        chartOptions = {
          xAxes: [{
            stacked: true
          }],
          yAxes: [{
            stacked: true,
            ticks: {
              beginAtZero: true,
              padding: 25
            }
          }]
        }
      } else {
        if (this.chartType === 'bar') {
          chartData = this.initChartDataForBar()
        } else if (this.chartType === 'pie') {
          chartData = this.initChartDataForPie()
        } else if (this.chartType === 'line') {
          chartData = this.initChartDataForLine()
        }

        chartType = this.chartType
        chartOptions = {
          yAxes: [{
            ticks: {
              beginAtZero: true,
              padding: 25
            }
          }]
        }
      }

      const ctx = document.getElementById(chartId)
      // eslint-disable-next-line
      new Chart(ctx, {
        type: chartType,
        data: chartData,
        options: {
          legend: { display: this.showLegend },
          responsive: true,
          lineTension: 1,
          scales: chartOptions
        }
      })
    }
  }
}
</script>

<style>

</style>
