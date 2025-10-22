package hello.core.scope;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Test;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Scope;

import jakarta.annotation.PostConstruct;
import jakarta.annotation.PreDestroy;

public class PrototypeTest {
	
	@Test
	void prototypeBeanFind() {
		AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(PrototypeBean.class);
		PrototypeBean prototypeBean1 = ac.getBean(PrototypeBean.class);
		PrototypeBean prototypeBean2 = ac.getBean(PrototypeBean.class);
		System.out.println("prototypeBean1: " + prototypeBean1);
		System.out.println("prototypeBean2: " + prototypeBean2);
		assertThat(prototypeBean1).isNotSameAs(prototypeBean2);
//		ac.close();
		prototypeBean1.destroy();
		prototypeBean2.destroy();
	}
	
	@Scope("prototype")
	static class PrototypeBean {
		@PostConstruct
		public void init() {
			System.out.println("PrototypeBean.init()");
		}
		
		@PreDestroy
		public void destroy() {
			System.out.println("PrototypeBean.destroy()");
		}
	}

}
