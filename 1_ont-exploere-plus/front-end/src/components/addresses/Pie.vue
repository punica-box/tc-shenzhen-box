<script>
import { polarArea } from 'vue-chartjs'

export default {
  extends: polarArea,
  props: ['chartdata', 'options'],
  mounted () {
    this.renderChart(this.chartdata, this.options)
  }
}
</script>

<style>
</style>