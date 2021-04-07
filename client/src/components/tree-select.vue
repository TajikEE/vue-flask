<template>
  <treeselect
    :value="sectors"
    @input="updateSectors = $event"
    :multiple="true"
    :options="OPTIONS_DATA"
  />
</template>

<script>
import Treeselect from "@riophae/vue-treeselect";
import "@riophae/vue-treeselect/dist/vue-treeselect.css";
import { OPTIONS_DATA } from "../helpers/options-data";

export default {
  props: {
    sectors: null,
  },

  data: () => ({
    updateSectors: null,
  }),

  watch: {
    updateSectors(val) {
      this.$emit("updatedSectors", val);
    },
  },

  computed: {
    OPTIONS_DATA: () => OPTIONS_DATA,
  },

  components: {
    Treeselect,
  },
};
</script>
