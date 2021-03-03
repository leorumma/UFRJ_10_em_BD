<template>
  <b-container>
    <b-row>
      <div>
        <b-button
          class="mb-4"
          :variant="isRealData ? 'outline-primary' : 'primary'"
          @click="changeCharts(true)"
        >
          Dados Reais
        </b-button>

        <b-button
          class="mb-4"
          :variant="!isRealData ? 'outline-primary' : 'primary'"
          @click="changeCharts(false)"
        >
          Dados Simulados
        </b-button>
      </div>
    </b-row>

    <div v-show="isRealData">
      <b-row
        class="mb-4"
        v-for="i in Math.ceil(realDataCharts.length / 2)"
        :key="i"
      >
        <b-col
          :sm="chart.tipo == 'pie' ? 6 : 12"
          v-for="(chart, key) in realDataCharts.slice((i - 1) * 2, i * 2)"
          :key="key"
        >
          <chart
            :item="chart.index"
            :chartType="chart.tipo"
            :chartLabel="chart.titulo"
            :data="chart.dados"
          />
        </b-col>
      </b-row>
    </div>

    <div v-show="!isRealData">
      <b-row
        class="mb-4"
        v-for="i in Math.ceil(simulatedDataCharts.length / 2)"
        :key="i"
      >
        <b-col sm="6" v-for="(chart, key) in simulatedDataCharts.slice((i - 1) * 2, i * 2)" :key="key">
          <chart
            :item="chart.index"
            :chartType="chart.tipo"
            :chartLabel="chart.titulo"
            :data="chart.dados"
          />
        </b-col>
      </b-row>
    </div>
  </b-container>
</template>

<script>
import Chart from '../components/Chart'

import { API_PATH, get } from '../helpers/api'

export default {

  components: {
    Chart
  },

  data () {
    return {
      isRealData: true,
      chartIndex: 0,

      realDataCharts: [],
      simulatedDataCharts: []
    }
  },

  created () {
    this.getCharts()
  },

  methods: {
    changeCharts (isRealData) {
      this.isRealData = isRealData

      if (!this.isRealData && this.simulatedDataCharts.length === 0) {
        this.getCharts()
      }
    },

    getCharts () {
      let url = '/mainpage'

      if (this.isRealData) {
        url += '?simulated=0/'
      } else {
        url += '?simulated=1/'
      }

      get({
        url: API_PATH + url,
        success: data => {
          for (let content of data.content) {
            // percorre a resposta colocando os dados no padrao
            // para o grafico ser desenhado

            for (let chartData of content.children) {
              let chart = {
                index: this.chartIndex,
                titulo: chartData.title,
                tipo: chartData.type,
                dados: []
              }

              if (chart.tipo === 'stacked bar') {
                chart.dados = {
                  labels: chartData.content.labels,
                  datasets: chartData.content.datasets
                }
              } else {
                for (let label in chartData.content) {
                  chart.dados.push({ label: label, value: chartData.content[label] })
                }
              }

              if (this.isRealData) {
                this.realDataCharts.push(chart)
              } else {
                this.simulatedDataCharts.push(chart)
              }

              this.chartIndex++
            }
          }
        }
      })

    }
  }

}
</script>

<style>

</style>
