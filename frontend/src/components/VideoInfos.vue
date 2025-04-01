<template>
  <a :href="video.url" target="_blank">
    <div class="video-wrapper">
      <img :src="video.thumbnail_url" class="video-thumbnail"/>
      <div class="video-text-wrapper">
        <h3>{{ video.title }}</h3>
        <p>By {{ video.user_name }}</p>
      </div>
    </div>
  </a>
</template>

<script>
  export default {
    props: {
      video: Object,
    },
  };
</script>
