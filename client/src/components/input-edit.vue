<template>
  <div :class="$style.root" @click.stop>
    <input
      :class="$style.input"
      :size="innerValue.length"
      @input="$emit('input', innerValue)"
      @keyup.enter="submit"
      @keyup.esc="cancel"
      autocomplete="nope"
      minlength="1"
      ref="input"
      v-model="innerValue"
    />
  </div>
</template>

<script>
import Vue from "vue";

export default Vue.extend({
  props: {
    value: null,
  },

  data: () => ({
    innerValue: null,
  }),

  watch: {
    value: {
      handler(value) {
        this.innerValue = value;
      },
      immediate: true,
    },
  },

  methods: {
    submit() {
      this.$emit("submit");

      this.$refs.input.blur();
    },
  },
});
</script>

<style lang="scss" module>
.root {
  position: relative;
  display: flex;
  align-items: center;
}

.input {
  background: #fcfcfc;
  border: 1px solid #ddd;
  border-radius: 0.3125rem;
  padding: 0.5rem;
  width: auto;
  outline: none;
  max-width: 100%;
}
</style>
