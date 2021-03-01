<template>
  <b-container>
    <b-row
      :class="{ 'mt-4': i > 1 }"
      v-for="i in Math.ceil(charts.length / 2)"
      :key="i"
    >
      <b-col sm="6" v-for="(chart, key) in charts.slice((i - 1) * 2, i * 2)" :key="key">
        <chart
          :item="(i-1)*2 + key"
          :chartType="chart.tipo"
          :chartLabel="chart.titulo"
          :data="chart.dados"
        />
      </b-col>
    </b-row>

    <b-row class="mt-4 mb-5" v-for="i in Math.ceil(charts_example.length / 2)" :key="charts.length + i">
      <b-col sm="6" v-for="(chart, key) in charts_example.slice((i - 1) * 2, i * 2)" :key="key">
        <chart
          :item="(i-1)*2 + key + charts.length"
          chartType="stacked bar"
          :chartLabel="chart.titulo"
          :data="chart.dados"
        />
      </b-col>
    </b-row>

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
      charts_example: [],
      charts: []
    }
  },

  created () {
    this.getCharts()
  },

  methods: {
    getCharts () {
      get({
        url: `${API_PATH}/mainpage/`,
        success: data => {
          // percorre a resposta colocando os dados no padrao
          // para o grafico ser desenhado
          for (let content of data.content) {

            for (let chartData of content.children) {
              let chart = { titulo: chartData.title, tipo: chartData.type, dados: [] }

              for (let label in chartData.content) {
                chart.dados.push({ label: label, value: chartData.content[label] })
              }

              this.charts.push(chart)
            }

          }
        }
      })

      get({
        url: `${API_PATH}/teste/`,
        success: data => {
          for (let content of data.content) {

            for (let chartData of content.children) {
              let chart = {
                titulo: chartData.title,
                tipo: chartData.type,
                dados: {
                  labels: chartData.content.labels,
                  datasets: chartData.content.datasets
                }
              }

              this.charts_example.push(chart)
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
