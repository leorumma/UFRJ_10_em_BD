<template>
  <b-container>
    <b-row v-for="i in Math.ceil(charts.length / 2)" :key="i">
      <b-col
        :class="{ 'mt-4': i > 1 }"
        v-for="(chart, key) in charts.slice((i - 1) * 2, i * 2)"
        :key="key"
      >
        <chart
          :item="(i-1)*2 + key"
          chartType="pie"
          :chartLabel="`Teste ${(i-1)*2 + key + 1}`"
          :data="chart.dados"
        />
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Chart from '../components/Chart'

export default {

  components: {
    Chart
  },

  data () {
    return {
      charts: [
        { dados: [
          { label: '20 anos', value: 200 },
          { label: '30 anos', value: 325 },
          { label: '40 anos', value: 750 },
          { label: '50 anos', value: 1230 }
        ] },
        { dados: [
          { label: '20 anos', value: 200 },
          { label: '30 anos', value: 325 },
          { label: '40 anos', value: 750 },
          { label: '50 anos', value: 1230 }
        ] },
        { dados: [
          { label: '20 anos', value: 200 },
          { label: '30 anos', value: 325 },
          { label: '40 anos', value: 750 },
          { label: '50 anos', value: 1230 }
        ] },
        { dados: [
          { label: '20 anos', value: 200 },
          { label: '30 anos', value: 325 },
          { label: '40 anos', value: 750 },
          { label: '50 anos', value: 1230 }
        ] }
      ]
    }
  }

}
</script>

<style>

</style>
