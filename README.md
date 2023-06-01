# Tools

## Synthetics2Jetpack
1. ```
private lateinit var binding: Binding
binding = Binding.inflate(layoutInflater)

//val binding = ActivityEventBinding.inflate(activity.layoutInflater, parent, false)
//View inflate(int resource, ViewGroup root)
//View inflate(int resource, ViewGroup root, boolean attachToRoot)

setContentView(binding.root)

ViewDataBinding
```
2. Replace `setContentView(R.layout)`

2. [Migrate from Kotlin synthetics to Jetpack view binding](https://developer.android.com/topic/libraries/view-binding/migration)