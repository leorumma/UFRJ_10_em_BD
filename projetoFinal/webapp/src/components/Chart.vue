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
      type: Array,
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
    initChartData () {
      let chart = {
        labels: [],
        datasets: [{
          label: this.chartLabel,
          data: [],
          borderWidth: 3,
          backgroundColor: ['#FF6384', '#FF9F40', '#36A2EB', '#4BC0C0', '#FFCD56']
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
      if (this.data.length < 1) {
        return
      }

      let chartData = this.initChartData()

      const ctx = document.getElementById(chartId)
      new Chart(ctx, {
        type: this.chartType,
        data: chartData,
        options: {
          responsive: true,
          lineTension: 1,
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true,
                padding: 25
              }
            }]
          }
        }
      })
    }
  }
}
</script>

<style>

</style>
