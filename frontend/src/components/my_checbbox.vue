Vue.component('my-checkbox', {
  template: `
  		<div class="my-check-box">
      	<label>{{label}}</label>
    		<input type="checkbox" :value="val" v-model="checked" @change="onChange" />
      </div>`,
  props: ['value', 'val', 'label'],
  data () {
    return {
      checkedProxy: false
    }
  },
  computed: {
	  checked: {
      get () {
        return this.value
      },
      set (val) {
        this.checkedProxy = val
      }
    }
  },
  methods: {
    onChange: function(e) {
      this.$emit('input', this.checkedProxy)
    }
  }
}),